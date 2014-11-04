""" Data from Livermore 1908 """
import re
from os import path
from datetime import datetime as datetime_
from datetime import date as date_
import codecs
import sys
import csv

import sqlalchemy as sa
import yaml

from acwbdb import config
from acwbdb import model

ASSAULT_RESULTS = ("Success", "Partial Success", "Failure")

BATTLE_RESULTS = ("Defeat", "Rout", "Victory", "Retired")
""" Acceptable values for us_result and cs_result"""

def load_table_a(src):
    """ Load Table A """
    session = model.Session()
    for row in csv.DictReader(src, delimiter='\t'):
        for x in ['us_losses_p1000', 'us_hits_p1000',
                  'cs_losses_p1000', 'cs_hits_p1000', 'page', 'row']:
            del row[x]
        row['start_date'] = datetime_.strptime(row['start_date'], "%Y-%m-%d").date()
        if row['end_date']:
            row['end_date'] = datetime_.strptime(row['end_date'], "%Y-%m-%d").date()
        else:
            row['end_date'] = row['start_date']
        battle = re.sub(" ", "_", "%s %s" %
                        (row['battle_name'], row['start_date']))
        session.add(model.LivBattle(battle = battle,
                           battle_name = row['battle_name'],
                           start_date = row['start_date'],
                           end_date = row['end_date']))
        session.add(model.LivForce(battle = battle,
                          combatant = u"US",
                          hit = row['us_hit'],
                          force = row['us_force']))
        session.add(model.LivForce(battle = battle,
                          combatant = u"CS",
                          hit = row['cs_hit'],
                          force = row['cs_force']))
    session.commit()
        
def load_confederate_results(src):
    """ Load data from Confederate results"""
    session = model.Session()
    reader = csv.DictReader(src, delimiter = '\t')
    for row in reader:
        force = session.query(model.LivForce).\
                 filter(model.LivForce.battle == row['battleid']).\
                 filter(model.LivForce.combatant == "CS").one()
        force.result = row['result']
        session.add(force)
    session.commit()

def load_union_results(src):
    """ Load data from Confederate results"""
    session = model.Session()
    reader = csv.DictReader(src, delimiter = '\t')
    for row in reader:
        force = session.query(model.LivForce).\
                 filter(model.LivForce.battle == row['battleid']).\
                 filter(model.LivForce.combatant == "US").one()
        force.result = row['result']
        session.add(force)
    session.commit()
        
        
def load_assaults(src):
    """ Load data on Assaults on Fortified Lines"""
    session = model.Session()
    reader = csv.DictReader(src, delimiter = '\t')
    for row in reader:
        battle = session.query(model.LivBattle).\
                 filter(model.LivBattle.battle == row['battleid']).one()
        battle.assault = True
        battle.us_attack = row['attacker'] == u"US"
        battle.assault_result = row['result']
        session.add(battle)
    session.commit()
    for battle in session.query(model.LivBattle).\
            filter(model.LivBattle.assault == None):
        battle.assault = False
        session.add(battle)
    session.commit()

def load_army_size(src):
    session = model.Session()
    for row in csv.DictReader(src):
        obj = model.LivArmySize()
        obj.date = datetime_.strptime(row['date'], "%Y-%m-%d").date()
        obj.union = row['No. on Union Rolls']
        obj.confed = row['No. on Confederate Returns']
        session.add(obj)
    session.commit()

def load_misc(src):
    data = yaml.load(src)
    session = model.Session()
    ## Add parents
    for parent, children in data['children'].items():
        for child in children:
            battle = session.query(model.LivBattle).\
                     filter(model.LivBattle.battle == child).one()
            battle.parent = parent
            session.add(battle)
    ## Add campaigns
    for battle in session.query(model.LivBattle):
        battle.campaign = (battle in data['campaigns'])
        session.add(battle)
    session.commit()

def load_links(infn):
    model.LivToDbpedia.load_from_file(infn)
    model.LivToCwsac.load_from_file(infn)

def load(datadir):
    print("loading liv_*")
    load_table_a(open(path.join(datadir, 'livermore', 'Table_A.tsv'), 'r'))
    load_confederate_results(open(path.join(datadir, 'livermore',
                                            'Confederate_Results.tsv'), 'r'))
    load_union_results(open(path.join(datadir, 'livermore',
                                      'Union_Results.tsv'), 'r'))
    load_assaults(open(path.join(datadir, 'livermore',
                                 'Assaults_on_Fortified_Lines.tsv'), 'r'))
    load_misc(open(path.join(datadir, 'livermore',
                             'misc.yaml'), 'r'))
    load_army_size(open(path.join(datadir, 'livermore',
                                  'liv_army_sizes.csv'), 'r'))
    # load_links(path.join(datadir, 'livermore', 'liv_links.yaml'))

def main():
    engine, datadir = sys.argv[1:3]
    model.Session.configure(bind = sa.create_engine(engine))
    load(datadir)

if __name__ == '__main__':
    main()
