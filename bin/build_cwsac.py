#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Build cwsac data """
import json
import csv
import os
import sys
import shutil
from os import path

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

battle_fields = (#'cwsac_reference',
    'battle',
    'url',
    'battle_name',
    'other_names',
    'state',
    'locations',
    'campaign',
    'start_date',
    'end_date',
    'operation',
    'assoc_battles',
    'results_text',
    'result',
    'forces_text',
    'strength',
    'casualties_text',
    'casualties',
    'description',
    'preservation',
    'significance'
)

# keys = set()
# for battle, battle_data in data.items():
#     for k in battle_data:
#         keys.add(k)
# print(keys)

def battle_csv(data, filename):
    with open(filename, 'w', encoding = 'utf-8') as f:
        writer = csv.DictWriter(f, battle_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            row = dict_subset(battle_data, battle_fields)
            row['operation'] = int(row['operation'])
            if row['other_names']:
              row['other_names'] = '; '.join(row['other_names'])
            row['locations'] = '; '.join(x['place'] + ', ' + x['state']
                                         for x in battle_data['location'])
            writer.writerow(row)

belligerent_fields = [
 'battle',
 'belligerent',
 'description',
 'strength_min',
 'strength_max',
 'armies',
 'corps',
 'divisions',
 'brigades',
 'regiments',
 'companies',

 'cavalry_regiments',
 'cavalry_brigades',
 'cavalry_corps',
 'cavalry_divisions',

 'artillery_batteries',
 'ships',
 'ironclads',
 'gunboats',
 'wooden_ships',
 'rams',

 'casualties',
 'killed',
 'wounded',
 'missing',
 'captured',

]

def forces_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, belligerent_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            for belligerent, x in sorted(battle_data['belligerents'].items()):
                row = dict_subset(x, belligerent_fields)
                row['battle'] = battle
                row['belligerent'] = belligerent
                writer.writerow(row)

commanders_fields = (
    'battle',
    'belligerent',
    'fullname',
    'rank',
    'navy',
    'first_name',
    'last_name',
    'middle_name',
    'suffix'
)

def commanders_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, commanders_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            for belligerent, x in sorted(battle_data['belligerents'].items()):
                for commander in x['commanders']:
                    row = commander.copy()
                    row['battle'] = battle
                    row['belligerent'] = belligerent
                    row['navy'] = int(row['navy'])
                    writer.writerow(row)

def copy_preservation(src, dst):
    shutil.copy(path.join(src, 'preservation.csv'),
                path.join(dst, 'cwsac_preservation.csv'))

def copy_significance(src, dst):
    shutil.copy(path.join(src, 'significance.csv'),
                path.join(dst, 'cwsac_significance.csv'))
    
def copy_theaters(src, dst):
    shutil.copy(path.join(src, 'theaters.csv'),
                path.join(dst, 'cwsac_theaters.csv'))

def copy_campaigns(src, dst):
    shutil.copy(path.join(src, 'campaigns.csv'),
                path.join(dst, 'cwsac_campaigns.csv'))

def copy_cwsac_to_dbpedia(src, dst):
    shutil.copy(path.join(src, 'cwsac_to_dbpedia.csv'),
                path.join(dst, 'cwsac_to_dbpedia.csv'))

def copy_json(data, dst):
    with open(path.join(dst, 'cwsac.json'), 'w') as f:
        json.dump(data, f)
            
def build(SRC, DST):
    data = {}
    data_dir = path.join(SRC, 'json')
    for filename in os.listdir(data_dir):
        with open(path.join(data_dir, filename), 'r') as f:
            data[path.splitext(filename)[0]] = json.load(f)
            
    battle_csv(data, path.join(DST, 'cwsac_battles.csv'))
    forces_csv(data, path.join(DST, 'cwsac_forces.csv'))
    commanders_csv(data, path.join(DST, 'cwsac_commanders.csv'))
    copy_campaigns(SRC, DST)
    copy_theaters(SRC, DST)
    copy_significance(SRC, DST)
    copy_preservation(SRC, DST)
    copy_json(data, DST)

def main():
    SRC = sys.argv[1]
    DST = sys.argv[2]
    build(SRC, DST)

if __name__ == "__main__":
    main()
                   