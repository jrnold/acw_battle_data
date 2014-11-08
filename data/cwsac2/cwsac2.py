# -*- coding: utf-8 -*-
"""

Files

- strengths.yaml: parsed strengths
- battlefield_area_statistics.txt: battlefield area sizes

""" 
from os import path
import codecs
import csv
import glob
import json
import re
import sys
import datetime

import yaml

import pyparsing as pp

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


def parse_date_range(x, hyphen=u"- — –", comma=u","):
    """Parse Date Ranges

    Parse date ranges like

    January 1-5, 1900
    January 1-March 1, 1900
    January 1 1900 - March 5, 1900

    """
    months = {'April': 4,
              'August': 8,
              'December': 12,
              'February': 2,
              'January': 1,
              'July': 7,
              'June': 6,
              'March': 3,
              'May': 5,
              'November': 11,
              'October': 10,
              'September': 9}
    comma = pp.oneOf(comma).suppress()
    hyphen = pp.oneOf(hyphen).suppress()
    month = pp.oneOf([k for k in months.keys()])
    month = month.setResultsName('m')
    month.addParseAction(lambda s,l,t: [months[t[0]]])
    day = pp.Word(pp.nums).setResultsName('d')
    day.addParseAction(lambda s,l,t: [int(t[0])])
    year = pp.Word(pp.nums).setResultsName('year')
    year.addParseAction(lambda s,l,t: [int(t[0])])

    start_date = (month + day + pp.Optional(comma + year)).setResultsName('start')
    start_date = (month + day + pp.Optional(comma + year)).setResultsName('start')
    end_date = (pp.Optional(month) + day + comma + year).setResultsName('end')
    date_range = start_date + pp.Optional(hyphen + end_date)
    # date_range needs to be first or one_date will pick up
    # start_dates with a year
    grammar =  date_range
    toks = grammar.parseString(x).asDict()
    d0 = toks['start']
    d1 = toks['end'] if 'end' in toks else d0
    if 'year' not in d0:
        d0['year'] = d1['year']
    if 'm' not in d1:
        d1['m'] = d0['m']
    d0date = datetime.date(*(d0[x] for x in ('year', 'm', 'd')))
    d1date = datetime.date(*(d1[x] for x in ('year', 'm', 'd')))
    return (d0date, d1date)


def page2battle(page, results, strengths, areas, infn):
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
    data['results'] = results[data['results_text']]
    study_area = re.sub(',', '', page[13].split(' ')[0])
    if study_area in ['Not']:
        study_area = None
    else:
        study_area = float(study_area)
    data['study_area'] = study_area
    data['core_area'] = areas[battle]['core_area']
    data['potnr_boundary'] = areas[battle]['potnr_boundary']
    data['locations'] = []
    data['dates'] = []

    # Participants
    forces = {}
    if (re.search(r'\[I\]', commanders) is not None):
        forces['I'] = {'commanders': []}
    if (re.search(r'\[US\]', commanders) is not None):
        forces['US'] = {'commanders': []}
    if (re.search(r'\[CS\]', commanders) is not None):
        forces['CS'] = {'commanders': []}

    # strengths
    for k, v in strengths[battle].items():
        if k in ('US', 'CS', 'I'):
            for j, x in v.items():
                forces[k][j] = x
        else:
            data[k] = v
            
    # Commanders
    try:
        commanders = parse_commanders(commanders)
        for k, v in commanders.items():
            for x in v:
                forces[k]['commanders'].append({'fullname' : x['fullname'],
                                                'rank' : RANKS_LOOKUP[x['rank']]})
    except pp.ParseException:
        print("%s: %s" % (battle, commanders))

    data['combatants'] = forces

        # Location
    for i, loc in enumerate(location_text.split(';')):
        loc = loc.strip().split(',')
        if len(loc) == 1:
            location = loc[0]
            if location in ('Non determined', 'Undetermined'):
                location = None
            state = data['state']
            data['locations'].append({'location' : location,
                                      'state' : state})

        elif len(loc) == 2:
            location, state = loc
            data['locations'].append({'location' : location.strip(),
                                      'state' : state.strip()})
        else:
            print("%s: did not parse location: %s" % (battle, data['location']))

    
    for i, d in enumerate(page[5].split(' and ')):
        start_date, end_date = parse_date_range(d)
        data['dates'].append({'start_date' : '%d-%d-%d' % (start_date.year,
                                                           start_date.month,
                                                           start_date.day),
                              'end_date' : '%d-%d-%d' % (end_date.year,
                                                         end_date.month,
                                                         end_date.day),
                              #'end_date' : date_range[1].strftime("%Y-%m-%d"),
                              'spell' : i + 1})
    return (battle, data)
                    
def parse_cwsac2_report(infn, results, strengths, areas):
    ## Identifies pages as the start of a battle summary
    RE_BATTLE = re.compile(r"^.* \([A-Z]{2}[0-9]{3}\)\nLocation", re.M)
    with codecs.open(infn, 'r', 'utf-8') as f:
        filetxt = f.read().split('\x0c')
    battles = ([x.split('\n\n') for x in filetxt if RE_BATTLE.search(x)])
    data = {}
    for x in battles:
        k, v = page2battle(x, results, strengths, areas, infn)
        data[k] = v
    return data

def load_reports(directory, results, strengths, areas):
    filelist = glob.glob(path.join(directory, "*.txt"))
    data = {}
    for f in filelist:
        report = parse_cwsac2_report(f, results, strengths, areas)
        data.update(report)
    json.dump(data, open('cwsac2.json', 'w'), indent=2)

def load(datadir):
    directory = datadir
    strengths = yaml.load(open(path.join(directory, 'forces.yaml'), 'r'))
    areas = dict((x['battle'], x) for x in 
                 csv.DictReader(open(path.join(directory, 'battlefield_area_statistics.csv'), 'r')))
    results = yaml.load(open(path.join(directory, "results.yaml"), 'r'))
    load_reports(path.join(directory, 'reports'), results, strengths, areas)

def main():
    load('.')

if __name__ == '__main__':
    main()
