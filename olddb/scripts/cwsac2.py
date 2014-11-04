"""
The individual entries do not contain the Core Area values. These
are found in the ""Battlefield Area Statistics"" at the beginning
of each state's report.
""" 
import re
from os import path
import glob
import codecs
import sys
import csv

import yaml

import sqlalchemy as sa
from sqlalchemy.ext import declarative
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import types
import pyparsing as pp

from acwbdb import model
from acwbdb import util

URL_BASE = "http://www.nps.gov/hps/abpp/CWSII"

RANKS = {'Lieutenant': ['Lieutenant', 'Lt.'],
         'First Lieutenant': ['1st Lieutenant'],
         'Captain': ['Captain', 'Cpt.', 'Capt.'],
         'Brevet Major': ['Brevet Major'],
         'Major': ['Major', 'Maj.'],
         'Lieutenant Colonel': ['Lieutenant Colonel', 'Lt. Col.'],
         'Colonel': ['Colonel', 'Col.'],
         'Brigadier General': ['Brigadier General', 'Brig. Gen.'],
         'Lieutenant General': ['Lieutenant General', 'Lt. Gen.'],
         'Brevet Major General': ['Brevet Major General'],
         'Major General': ['Major General', 'Maj. Gen.'],
         'General': ['General', 'Gen.'],
         # Naval
         'Flag Officer': ['Flag Officer'],
         'Lieutenant Commander': ['Lieutenant Commander', 'Lt. Cdr.'],
         'Commander': ['Commander', 'Cdr.'],
         'Acting Master': ['Acting Master'],
         'Acting Rear Admiral': ['Acting Rear Admiral'],
         'Commodore': ['Commodore'],
         'Rear Admiral': ['Rear Admiral'],
         'Admiral': ['Admiral'],
         # American Indians commanders are all called 'Chief' in the data
         'Chief': ['Chief']}

RANKS_LOOKUP = {}
for k, v in RANKS.items():
    for x in v:
        RANKS_LOOKUP[x] = k


def parse_forces(x):
    """Parse force descriptions from cwsac:forces_engaged

    This parses forces engaged entries that have the orders of battle
    for both sides

    1st Regiment and 2nd Regiment [US]; 3rd Regiment [CS]

    """
    FORCES = ("US", "CS", "I")
    forces = '|'.join(FORCES)
    pat1 = (r"(?P<force1>.*)\[(?P<c1>%s)\]; (?P<force2>.*)\[(?P<c2>%s)\]" %
            (forces, forces))
    pat2 = (r"(?P<total>.*)(\((?P<force1>.*) (?P<c1>%s); (?P<force2>.*) (?P<c2>%s)\))" %
            (forces, forces))
    m1 = re.match(pat1, x)
    m2 = re.match(pat2, x)
    data = {}
    if m1:
        data[m1.group('c1')] = m1.group('force1').strip()
        data[m1.group('c2')] = m1.group('force2').strip()
        data['total'] = None
    elif m2:
        data['total'] = m2.group('total').strip()
        data[m2.group('c1')] = m2.group('force1').strip()
        data[m2.group('c2')] = m2.group('force2').strip()
    else:
        data['total'] = x
        #print("Did not match forces: %s" % x)
    return data


def parse_commanders(x):
    # Grammar
    LBRAK, RBRAK, COMMA = (pp.Literal(x).suppress() for x in "[],")
    AND = pp.Literal("and").suppress()
    and_ = pp.Optional(COMMA) + AND
    RANK = pp.Or(pp.Literal(x) for x in RANKS_LOOKUP.keys())("rank")
    NAME = pp.Word(pp.srange("[A-Z]"), pp.alphas + pp.alphas8bit, min=2)
    ABBR = pp.Regex(r"([A-Z]\.)+")
    SUFFIX = pp.Literal("Jr.")
    NOCMDR = (pp.Literal("None"))("none")
    COMBATANT = pp.oneOf(' '.join(('US', 'CS', 'I')))("combatant")
    
    nametoken = ABBR | pp.quotedString | NAME
    name = (pp.OneOrMore(nametoken) + pp.Optional(pp.Literal(",") + SUFFIX))("fullname")
    name.addParseAction(lambda s,l,t: ' '.join(t))
    
    cmdrname = RANK + name 
    commander = pp.Group(cmdrname | NOCMDR)
    commander_list = pp.Group(pp.delimitedList(commander, ",") +
                              pp.Optional(and_ + commander))("commanders")
    milforce = pp.Group(commander_list + LBRAK + COMBATANT + RBRAK)
    grammar = pp.delimitedList(milforce, ";")
    toks = grammar.parseString(x)

    # A smarter grammar could probably have avoided this
    res = {}
    for _force in toks:
        k = _force['combatant']
        res[k] = [x.asDict() for x in _force['commanders']
                  if "none" not in x.asDict()]
    return res

def page2battle(session, page, resultdict, infn):
    def clean(x):
        return re.sub(' +', ' ', re.sub('\n', ' ', x))
    data = {}
    data['battle_name'], data['battle'] = re.match(r"(.*) \(([A-Z]{2}[0-9]{3})\)", page[0]).groups()
    battle = data['battle']
    data['state'] = data['battle'][:2]
    data['url'] = URL_BASE + '/' + path.splitext(path.basename(infn))[0] + '.pdf'
    location_text = clean(page[1])
    data['campaign'] = clean(page[3])
    commanders = clean(page[7])
    data['forces_text'] = clean(page[9])
    data['results_text'] = clean(page[11])
    data['results'] = resultdict[data['results_text']]
    study_area = re.sub(',', '', page[13].split(' ')[0])
    if study_area in ['Not']:
        study_area = None
    else:
        study_area = float(study_area)
    data['study_area'] = study_area
    # Participants
    forces = {}
    if (re.search(r'\[I\]', commanders) is not None):
        forces['I'] = model.Cwsac2Force(forceid = battle + "/I",
                                          battle = battle,
                                          combatant = "I")
    if (re.search(r'\[US\]', commanders) is not None):
        forces['US'] = model.Cwsac2Force(forceid = battle + "/US",
                                           battle = battle,
                                           combatant = "US")
    if (re.search(r'\[CS\]', commanders) is not None):
        forces['CS'] = model.Cwsac2Force(forceid = battle + "/CS",
                                           battle = battle,
                                           combatant = "CS")

    # Location
    for i, loc in enumerate(location_text.split(';')):
        loc = loc.strip().split(',')
        if len(loc) == 1:
            location = loc[0]
            if location in ('Non determined', 'Undetermined'):
                location = None
            state = data['state']
            session.add(model.Cwsac2Location(battle = battle,
                                             locnum = i,
                                             location = location,
                                             state = state))
        elif len(loc) == 2:
            location, state = loc
            session.add(model.Cwsac2Location(battle = battle,
                                             locnum = i,
                                             location = location.strip(),
                                             state = state.strip()))
        else:
            print("%s: did not parse location: %s" % (battle, data['location']))

    # Forces
    forces_text = parse_forces(data['forces_text'])
    if 'total' in forces_text:
        data['forces'] = forces_text['total']
    for x in ('US', 'CS', 'I'):
        if x in forces and x in forces_text:
            setattr(forces[x], 'forces', forces_text[x])

    # Commanders
    try:
        commanders = parse_commanders(commanders)
        for k, v in commanders.items():
            for x in v:
                cmdr = model.Cwsac2Commander(forceid = battle + '/' + k,
                                      fullname = x['fullname'],
                                      rank = RANKS_LOOKUP[x['rank']])
                session.add(cmdr)
        #print(commanders)
    except pp.ParseException:
        print("%s: %s" % (battle, commanders))

    session.add(model.Cwsac2Battle(**data))
    session.add_all(forces.values())

    for i, d in enumerate(page[5].split(' and ')):
        date_range = util.parse_date_range(d)
        session.add(model.Cwsac2BattleDate(battle = data['battle'],
                                           start_date = date_range[0],
                                           end_date = date_range[1],
                                           spell = i + 1))

                    
def parse_cwsac2_report(session, infn, resultdict):
    ## Identifies pages as the start of a battle summary
    RE_BATTLE = re.compile(r"^.* \([A-Z]{2}[0-9]{3}\)\nLocation", re.M)
    with codecs.open(infn, 'r', 'utf-8') as f:
        filetxt = f.read().split('\x0c')
    battles = ([x.split('\n\n') for x in filetxt if RE_BATTLE.search(x)])
    for x in battles:
        page2battle(session, x, resultdict, infn)

def load_reports(directory, results):
    resultdict = yaml.load(results)
    filelist = glob.glob(path.join(directory, "*.txt"))
    session = model.Session()
    for f in filelist:
        parse_cwsac2_report(session, f, resultdict)
    session.commit()

def add_area(src):
    RE_AREA = re.compile(r"(.*) \([A-Z]{2}[0-9]{3}\) (.*) (.*) (.*)")
    session = model.Session()
    reader = csv.DictReader(src, delimiter=' ')
    for row in reader:
        battle = session.query(model.Cwsac2Battle).\
                 filter(model.Cwsac2Battle.battle == row['battle']).one()
        for k, v in row.items():
            if v == "NA":
                row[k] = None
        for k, v in row.items():
            if k not in ['battle']:
                setattr(battle, k, v)
    session.commit()

def add_strengths(src):
    session = model.Session()
    strengths = yaml.load(src)
    for battle, data in strengths['battles'].items():
        btl = session.query(model.Cwsac2Battle).\
              filter(model.Cwsac2Battle.battle == battle).one()
        btl.strength = data['strength']
    for forceid, data in strengths['forces'].items():
        force = session.query(model.Cwsac2Force).\
                filter(model.Cwsac2Force.forceid == forceid).one()
        force.strength = data['strength']
    session.commit()

def load(datadir):
    print("loading cwsac2_*")
    directory = path.join(datadir, 'cwsac2')
    load_reports(path.join(directory, 'reports'),
                 open(path.join(directory, 'results.yaml')))
    add_area(open(path.join(directory,
                            'battlefield_area_statistics.txt'), 'r'))
    add_strengths(open(path.join(directory, 'strengths.yaml'), 'r'))

def main():
    engine, datadir = sys.argv[1:3]
    model.Session.configure(bind = sa.create_engine(engine))
    load(datadir)

if __name__ == '__main__':
    main()
