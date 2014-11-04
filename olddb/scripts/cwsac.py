#!/usr/bin/env python3
""" Load CWSAC data

Loads tables

- 

This does not clean up the fields at all.
"""

import json
import sys
from datetime import datetime as datetime_
from os import path
import calendar

import sqlalchemy as sa

from acwbdb import model

def subset(d, keys):
    return dict((k, d[k]) for k in d if k in keys)

def forceid(force, combatant):
    return force + '/' + combatant

def load_battles(session, data):
    print("loading data into table %s" % model.CwsacBattle.__table__)
    cols = [c.name for c in model.CwsacBattle.__table__.c]
    for k, v in data.items():
        battle = v.copy()
        battle['start_date'] =  datetime_.strptime(battle['start_date'], "%Y-%m-%d").date()
        battle['end_date'] =  datetime_.strptime(battle['end_date'], "%Y-%m-%d").date()
        session.add(model.CwsacBattle(**subset(battle, cols)))

def load_forces(session, data):
    print("loading data into table %s" % model.CwsacForce.__table__)
    for battle, v in data.items():
        for combatant, v2 in v['forces'].items():
            force = v2.copy()
            force['forceid'] = forceid(battle, combatant)
            force['combatant'] = combatant
            force['battle'] = battle
            del force['commanders']
            session.add(model.CwsacForce(**force))

def load_commanders(session, data):
    print("loading data into table %s" % model.CwsacCommander.__table__)
    for battle, v in data.items():
        for combatant, force in v['forces'].items():
            for cmdr in force['commanders']:
                cmdr['forceid'] = forceid(battle, combatant)
                session.add(model.CwsacCommander(**cmdr))
    
def main():
    engine, datadir = sys.argv[1:3]
    model.Session.configure(bind = sa.create_engine(engine))
    session = model.Session()
    cwsacdata = json.load(open(path.join(datadir, "cwsac/cwsac.json"), "r"))
    model.CwsacTheater.load_from_yaml(session, path.join(datadir, 'cwsac/theaters.yaml'))
    model.CwsacCampaign.load_from_csv(session, path.join(datadir, 'cwsac/campaigns.csv'))    
    load_battles(session, cwsacdata)
    load_forces(session, cwsacdata)
    load_commanders(session, cwsacdata)
    session.commit()

if __name__ == '__main__':
    main()
