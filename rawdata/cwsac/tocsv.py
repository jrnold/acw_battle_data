""" Convert cwsac.json to csv files """
import json
import csv
import os
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

SRC = "json"

data = {}
for filename in os.listdir(SRC):
    print(filename)
    with open(path.join(SRC, filename), 'r') as f:
        data[path.splitext(filename)[0]] = json.load(f)

battle_csv(data, 'cwsac_battles.csv')
forces_csv(data, 'cwsac_forces.csv')
commanders_csv(data, 'cwsac_commanders.csv')
