# -*- coding: utf-8 -*-
import json
from os import path
import glob
import datetime
import codecs

import sqlalchemy as sa
import yaml

from acward import model
from acward import config

COMBATANTS = {u"Unierte": "US",
              u"Konföderierte": "CS"}

BATTLE_TYPES = ('Schlacht',
                'Treffen',
                'Belagerung',
                'Einnahme',
                'Kapitulation')

def load_yaml_files(directory):
    data = {}
    for fn in glob.glob('%s/*.yaml' % directory):
        k = path.basename(fn)[:-5]
        with codecs.open(fn, 'r', encoding='utf-8') as f:
            data[k] = yaml.load(f)
    return data

def load_battles(data):
    session = model.Session()
    for k, v in data.iteritems():
        row = {}
        for cat in BATTLE_TYPES:
            if cat in v['category']:
                row[cat.lower()] = True
            else:
                row[cat.lower()] = False
        row['start_date'] = v['startDate']
        row['end_date'] = v['endDate']
        if not row['end_date']:
            row['end_date'] = row['start_date']
        row['ordnung'] = v['ordnung']
        row['battle'] = k
        row['battle_name'] = v['name']
        session.add(model.BodBattle(**row))
    session.commit()

def clean_force(x, battle, victor):
    x['battle'] = battle
    x['victor'] = victor
    x['combatant'] = COMBATANTS[x['country']]
    del x['country']
    for k in ('verl_an_trophaen', 'commander', 'gefallen_generale'):
        del x[k]
    return x

def load_forces(data):
    session = model.Session()
    for k, v in data.iteritems():
        battle = k
        for side in ('victor', 'loser'):
            victor = (side == 'victor')
            session.add(model.BodForce(**clean_force(v[side], battle, victor)))
    session.commit()


def load_links(infn):
    model.BodToDbpedia.load_from_file(infn)
    model.BodToCwsac.load_from_file(infn)

def load(datadir):
    data = load_yaml_files(path.join(datadir, 'bodart/yaml'))
    load_battles(data)
    load_forces(data)
    load_links(path.join(datadir, 'bodart/bod_links.yaml'))


