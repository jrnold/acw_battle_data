""" Data from Kennedy (1998)"""

from os import path

import sqlalchemy as sa
import yaml

from acward import config
from acward import model
from acward import csv2
from acward.util import toint

def row_to_battle(row):
    partic = row['partic']
    us_min = toint(row['US_min'])
    us_max = toint(row['US_max']) if row['US_max'] else toint(row['US_min'])
    cs_min = toint(row['CS_min'])
    cs_max = toint(row['CS_max']) if row['CS_max'] else toint(row['CS_min'])
    cas_i = toint(row['I'])
    cas_min = cas_max = None
    if row['total']:
        cas_min, cas_max = [row['total']]*2
    else:
        if partic == 'CS US':
            if us_min is not None and cs_min is not None:
                cas_min = us_min + cs_min
                cas_max = us_max + cs_max
        if partic == 'I US':
            if us_min is not None and cas_i is not None:
                cas_min = us_min + cas_i
                cas_max = us_max + cas_i            
        if partic == 'CS I':
            if cs_min is not None and cas_i is not None:
                cas_min = cs_min + cas_i
                cas_max = cs_max + cas_i            
    battle = row['cwsacid']
    data = {'battle' : battle.upper(),
            'casualties_min' : cas_min,
            'casualties_max' : cas_max,
            'us' : "US" in partic.split(),
            'cs' : "CS" in partic.split(),
            'indian' : "I" in partic.split()}
    return data

def row_to_forces(row):
    battle = row['cwsacid']
    forces = []
    partic = row['partic'].split()
    if 'US' in partic:
        cas_min = row['US_min']
        cas_max = row['US_max'] if row['US_max'] else row['US_min']
        us = {'forceid' : "%s-%s" % (battle, "US"),
              'battle' : battle.upper(),
              'combatant' : u"US",
              'casualties_min' : cas_min,
              'casualties_max' : cas_max}
        forces.append(us)
    if 'CS' in partic:
        cas_min = row['CS_min']
        cas_max = row['CS_max'] if row['CS_max'] else row['CS_min']
        cs = {'forceid' : "%s-%s" % (battle, "CS"),
              'battle' : battle.upper(),
              'combatant' : u"CS",
              'casualties_min' : cas_min,
              'casualties_max' : cas_max}
        forces.append(cs)
    if "I" in partic:
        ind = {'forceid' : "%s-%s" % (battle, "I"),
               'battle' : battle,
               'combatant' : u"I",
               'casualties_min' : row["I"],
               'casualties_max' : row["I"]}
        forces.append(ind)
    return forces

def load_battles(src):
    """Load data into ken_battles table"""
    session = model.Session()
    for row in csv2.DictReader(src, delimiter='\t'):
        session.add(model.KenBattle(**row_to_battle(row)))
    session.commit()

def load_forces(src):
    session = model.Session()
    for row in csv2.DictReader(src, delimiter='\t'):
        forces = row_to_forces(row)
        for x in forces:
            session.add(model.KenForce(**x))
    session.commit()            

def cwsac_links(src):
    """ Create Links between Kennedy and CWSAC ids

    Although Kennedy identifies battles by CWSACID, the casualty data for
    several battles are often combined, so the mapping between the IDs is not
    one to one.
    
    """
    session = model.Session()
    cwsac_ids = [x[0] for x in session.query(model.CwsacBattle.battle).all()]
    data = {}
    relations = yaml.load(src)
    for x in session.query(model.KenBattle.battle):
        if x.battle in relations:
            for edge in relations[x.battle]:
                session.add(model.KenToCwsac(battle = x.battle,
                                             relation = edge['relation'],
                                             cwsac = edge['cwsac'].upper()))
        else:
            if x.battle in cwsac_ids:
                session.add(model.KenToCwsac(battle = x.battle,
                                             relation = 'sameas',
                                             cwsac = x.battle))
    session.commit()

def dbpedia_links():
    session = model.Session()
    q = session.query(model.KenToCwsac, model.CwsacToDbpedia).\
        filter(model.KenToCwsac.cwsac == model.CwsacToDbpedia.battle)
    for i, row in enumerate(q.all()):
        ken, cws = row
        relation = ken.relation if cws.relation == 'sameas' else cws.relation
        session.add(model.KenToDbpedia(battle = ken.battle,
                                       relation = ken.relation,
                                       dbpedia = cws.dbpedia))
    session.commit()

def load(datadir):
    print("load ken_*")
    load_battles(open(path.join(datadir, 'kennedy',
                                'casualties.tsv'), 'r'))        
    load_forces(open(path.join(datadir, 'kennedy',
                               'casualties.tsv'), 'r'))
    cwsac_links(open(path.join(datadir, 'kennedy',
                               'ken_to_cwsac.yaml'), 'r'))
    dbpedia_links()

