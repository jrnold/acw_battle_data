import csv
import yaml
import json
import os
from os import path

def int_(x):
    try:
        return int(x)
    except ValueError:
        return None

with open('kennedy_battles.csv', 'r') as f:
    reader = csv.DictReader(f)
    battles = {}
    for row in reader:
        battle = row['battle']
        del row['battle']
        battles[battle] = row

with open('kennedy_casualties.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        partic = row['partic'].split()
        battle = row['battle']
        if battle not in battles:
            print(battle)
            continue
        battles[battle]['forces'] = {}
        battles[battle]['casualties_text'] = row['description']
        battles[battle]['casualties_min'] = int_(row['total_min'])
        battles[battle]['casualties_max'] = int_(row['total_max'])
        if 'US' in partic:
            battles[battle]['forces']['US'] = {}
            battles[battle]['forces']['US']['casualties_min'] = int_(row['us_kwm_min'])
            battles[battle]['forces']['US']['casualties_max'] = int_(row['us_kwm_max'])
            battles[battle]['forces']['US']['killed_wounded_min'] = int_(row['us_kw_min'])
            battles[battle]['forces']['US']['killed_wounded_max'] = int_(row['us_kw_max'])
            battles[battle]['forces']['US']['missing'] = int_(row['us_m'])
        if 'CS' in partic:
            battles[battle]['forces']['Confederate'] = {}
            battles[battle]['forces']['Confederate']['casualties_min'] = int_(row['cs_kwm_min'])
            battles[battle]['forces']['Confederate']['casualties_max'] = int_(row['cs_kwm_max'])
            battles[battle]['forces']['Confederate']['killed_wounded_min'] = int_(row['cs_kw_min'])
            battles[battle]['forces']['Confederate']['killed_wounded_max'] = int_(row['cs_kw_max'])
            battles[battle]['forces']['Confederate']['missing'] = int_(row['cs_m'])
        if 'I' in partic:
            battles[battle]['forces']['Native American'] = {}
            battles[battle]['forces']['Native American']['casualties_min'] = int_(row['i_kwm'])
            battles[battle]['forces']['Native American']['casualties_max'] = int_(row['i_kwm'])
            battles[battle]['forces']['Native American']['killed_wounded_min'] = None
            battles[battle]['forces']['Native American']['killed_wounded_max'] = None
            battles[battle]['forces']['Native American']['missing'] = None

with open('kennedy1997.yaml', 'w') as f:
    yaml.dump(battles, f, default_flow_style = False)
            
        
