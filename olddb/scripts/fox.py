""" Data from Dyer's Compendium """
from os import path
from datetime import datetime as datetime_
from datetime import date as date_
from datetime import timedelta
import collections
import re
import codecs

from lxml import etree
import sqlalchemy as sa
import pyparsing as pp

from acward import model
from acward import csv2

BATTLE_XML = "Perseus_text_2001.05.0068.xml"

_months = dict(zip(["Jan", "Feb", "March", "April", "May", "June",
                   "July", "Aug", "Sept", "Oct", "Nov", "Dec"],
                  range(1, 13)))

def parse_human_integer(x, sep=','):
    integer = pp.Word(pp.nums, min=1, max=3)
    integer3 = pp.Word(pp.nums, exact = 3)
    comma = pp.Literal(sep).suppress()
    human_int = pp.Combine(integer + pp.ZeroOrMore(comma + integer))
    human_int.setParseAction(lambda s, l, t: int(t[0]))
    return human_int.parseString(x)[0]

def flatten(x):
    """ Flatten list of lists

    Solution from
    http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python

    """
    return [item for sublist in x for item in sublist]

def load_forces(src):
    """ Load data into fox_forces """
    session = model.Session()
    for rowid, row in enumerate(csv2.DictReader(src, delimiter='\t')):
        del row['cwsac']
        for x in ['killed', 'wounded', 'missing', 'casualties']:
            if row[x]:
                row[x] = parse_human_integer(row[x])
        for x in ['start', 'end']:
            dateparts = [x + i for i in ('y', 'm', 'd')]
            row['%s_date' % x] = date_(*[int(row[y]) for y in dateparts])
            for y in dateparts:
                del row[y]
        row['aggrow'] = (row['aggrow'] == '1')
        milforce = model.FoxForce(battle = rowid, **row)
        session.add(milforce)
    session.commit()

def load_forces_2(src):
    """ Load data into fox_forces_2 """
    session = model.Session()
    reader = csv2.DictReader(src, delimiter='\t')
    for rowid, row in enumerate(reader):
        del row['cwsac']
        for x in ['killed', 'wounded', 'missing', 'casualties']:
            if row[x]:
                row[x] = parse_human_integer(row[x])
        for x in ['start', 'end']:
            dateparts = [x + i for i in ('y', 'm', 'd')]
            row['%s_date' % x] = date_(*[int(row[y]) for y in dateparts])
            for y in dateparts:
                del row[y]
        row['cavalry'] = (row['cavalry'] == '1')
        milforce = model.FoxForce2(battle = rowid, **row)
        session.add(milforce)
    session.commit()

def load_outcomes(src):
    """ Load data into fox_outcomes """
    session = model.Session()
    for rowid, row in enumerate(csv2.DictReader(src, delimiter='\t')):
        row['union_victory'] = (row['victor'] == 'Union')
        del row['victor']
        del row['cwsac']
        battle = model.FoxOutcome(battle = rowid, **row)
        session.add(battle)
    session.commit()

def load_fox_outcomes_to_cwsac(src):
    session = model.Session()
    battles = {}
    for rowid, row in enumerate(csv2.DictReader(src, delimiter='\t')):
        cwsac =  row['cwsac']
        if cwsac:
            battles[rowid] =  cwsac.split()
    cnt = collections.Counter()
    for x in flatten(battles.values()):
        cnt[x] += 1
    multibattles = [k for k, v in cnt.iteritems() if v > 1]
    for k, v in battles.iteritems():
        if len(v) > 1:
            for btl in v:
                session.add(model.FoxOutcomeToCwsac(battle = k,
                                              relation = 'super',
                                              cwsac = btl))
        else:
            btl = v[0]
            if btl in multibattles:
                relation = 'sub'
            else:
                relation = 'sameas'
            session.add(model.FoxOutcomeToCwsac(battle = k,
                                          relation = relation,
                                          cwsac = btl))
            session.commit()
    session.commit()

def load_fox_forces_to_cwsac(src):
    session = model.Session()
    battles = {}
    reader = csv2.DictReader(src, delimiter='\t')
    for rowid, row in enumerate(reader):
        cwsac =  row['cwsac']
        if cwsac:
            battles[rowid] =  cwsac.split()
    cnt = collections.Counter()
    for x in flatten(battles.values()):
        cnt[x] += 1
    multibattles = [k for k, v in cnt.iteritems() if v > 1]
    for k, v in battles.iteritems():
        if len(v) > 1:
            for btl in v:
                session.add(model.FoxForceToCwsac(battle = k,
                                              relation = 'super',
                                              cwsac = btl))
        else:
            btl = v[0]
            if btl in multibattles:
                relation = 'sub'
            else:
                relation = 'sameas'
            session.add(model.FoxForceToCwsac(battle = k,
                                          relation = relation,
                                          cwsac = btl))
    session.commit()

def load_fox_forces_2_to_cwsac(src):
    session = model.Session()
    battles = {}
    reader = csv2.DictReader(src, delimiter='\t')
    for rowid, row in enumerate(reader):
        cwsac =  row['cwsac']
        if cwsac:
            battles[rowid] =  cwsac.split()
    cnt = collections.Counter()
    for x in flatten(battles.values()):
        cnt[x] += 1
    multibattles = [k for k, v in cnt.iteritems() if v > 1]
    for k, v in battles.iteritems():
        if len(v) > 1:
            for btl in v:
                session.add(model.FoxForce2ToCwsac(battle = k,
                                                   relation = 'super',
                                                   cwsac = btl))
        else:
            btl = v[0]
            if btl in multibattles:
                relation = 'sub'
            else:
                relation = 'sameas'
            session.add(model.FoxForce2ToCwsac(battle = k,
                                               relation = relation,
                                               cwsac = btl))
    session.commit()


def parse_regimental_losses():
    orgNames = ["10th N. York Cavalry", "Purnell Legion (Md.)", "26th Illionis"]
    exclude = ["Cavalry:", "Regiment."]

    f = open(path.join(config.CONFIG.paths['data'], BATTLE_XML), 'r')
    tree = etree.parse(f)
    ch11 = tree.xpath(".//div1[@id='c.11']")[0]
    #milestone = ch11.xpath("//milestone[@n='6081']")
    table = ch11.xpath(".//table")[0]
    for row in table.findall("row"):
        cells = row.findall('cell')
        ## Remove footnotes
        notes = cells[0].findall("note")
        for x in notes:
            cells[0].remove(x)
        ## Classify rowtype
        tags = [x.tag for x in cells[0]]
        text = etree.tostring(cells[0], method='text').strip()
        if 'placeName' in tags:
            rowtype = 'battle'
        elif 'dateStruct' in tags:
            rowtype = 'date'
        elif 'orgName' in tags:
            rowtype = 'unit'
        else:
            if text in orgNames:
                rowtype = 'unit'
            elif text in exclude:
                rowtype = 'ignore'
            else:
                rowtype = 'battle'
        ## Process rowtypes
        if rowtype == 'battle':
            battle = text
            date = None
        elif rowtype == 'date':
            date = text
            #print battle, date
        elif rowtype == "unit":
            cells =  [etree.tostring(c, method="text", encoding='utf8') for c in cells]
            ## Fix a row with extra cells
            if len(cells) > 7:
                del cells[3]
                print cells
            data = dict(zip(('regiment', 'division', 'corps', 'killed',
                             'wounded', 'missing', 'casualties'), cells))

def load(datadir):
    print("loading fox_*")
    load_forces(open(path.join(datadir, 'fox', 'fox_forces.tsv'), 'r'))
    load_forces_2(open(path.join(datadir, 'fox', 'fox_forces_2.tsv'), 'r'))
    load_outcomes(open(path.join(datadir, 'fox', 'fox_outcomes.tsv'), 'r'))
    load_fox_outcomes_to_cwsac(open(path.join(datadir, 'fox', 'fox_outcomes.tsv'), 'r'))
        
    load_fox_forces_to_cwsac(open(path.join(datadir, 'fox', 'fox_forces.tsv'), 'r'))
    load_fox_forces_2_to_cwsac(open(path.join(datadir, 'fox', 'fox_forces_2.tsv'), 'r'))
