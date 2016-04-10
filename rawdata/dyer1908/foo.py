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
        battles[battle_id] = {'other_names': row['other_names']}

with open('dyer_to_cwsac.yaml', 'r') as f:
    data = yaml.load(f)
    
    

