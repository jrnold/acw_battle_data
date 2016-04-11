# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 00:05:01 2016

@author: jrnold
"""

import csv
import datetime
import yaml

battles = {}
with open('../../data/nps_battles.csv', 'r', encoding = 'utf-8') as f:
    for row in csv.DictReader(f):
        start_date = datetime.datetime.strptime(row['start_date'], '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(row['end_date'], '%Y-%m-%d').date()
        battle_id = row['cwsac_id']
        state = set([row['state']])
        name = row['battle_name']
        battles[battle_id] = {'start_date': start_date, 'end_date': end_date, 'state': state,
                              'battle_name': name, 'cwsac_id': battle_id,
                              'other_names': row['other_names']}

with open('../../data/cws2_locations.csv', 'r') as f:
    for row in csv.DictReader(f):
        try:
            battles[row['battle']]['state'].add(row['state'])
        except KeyError:
            print(row['battle'])

dyer = []
with open('../../data/dyer_engagements.csv', 'r', encoding = 'utf-8') as f:
    for row in csv.DictReader(f):
        row['start_date'] = datetime.datetime.strptime(row['start_date'], '%Y-%m-%d').date()
        row['end_date'] = datetime.datetime.strptime(row['end_date'], '%Y-%m-%d').date()
        dyer.append(row.copy())

matched_battles = []
for k, v in battles.items():
    v['state'] = list(v['state'])
    new_btl = {'battles_cwsac': [v], 'battles_from': []}
    for btl_from in dyer:
        if btl_from['start_date'] <= v['end_date'] and btl_from['end_date'] >= v['end_date'] and btl_from['state'] in v['state']:
            new_btl['battles_from'].append(btl_from)
    matched_battles.append(new_btl)

matched_battles = sorted(matched_battles, key = lambda x: x['battles_cwsac'][0]['start_date'])
matched_battles = [x for x in matched_battles if x['battles_cwsac'][0]['start_date'] > datetime.date(1864, 10, 19)]

noalias_dumper = yaml.dumper.SafeDumper
noalias_dumper.ignore_aliases = lambda self, data: True
with open('dyer_to_cwsac_new.yaml', 'w') as f:
    yaml.dump(matched_battles, f, Dumper = noalias_dumper, default_flow_style = False)
