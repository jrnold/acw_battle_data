""" Convert cwsac.json to csv files """
import json
import csv

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

battle_fields = (#'cwsac_reference',
          'battle',
          'battle_name',
          'start_date',
          'end_date',
          'state',
          'location',
          'other_names',
          'operation',
          'description',
          'casualties_text',
          'url',
          'strength',
          'campaign',
          'results_text',
          'significance',
          'results',
          'uri',
          'preservation',
          'forces_text',
          'casualties',
          'assoc_battles')

# keys = set()
# for battle, battle_data in data.items():
#     for k in battle_data:
#         keys.add(k)
# print(keys)

def battle_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, battle_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            row = dict_subset(battle_data, battle_fields)
            writer.writerow(row)

belligerent_fields = ['battle',
 'belligerent',
 'corps',
 'strength_min',
 'strength_max'
 'description',
 'killed',
 'divisions',
 'brigades',
 'ironclads',
 'cavalry_regiments',
 'cavalry_brigades',
 'cavalry_corps',
 'cavalry_divisions',
 'gunboats',
 'casualties',
 'companies',
 'missing',
 'armies',
 'artillery_batteries',
 'wounded',
 'captured',
 'wooden_ships',
 'rams',
 'regiments',
 # 'commanders',
 'ships',
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

commanders_fields = ('battle', 'belligerent', 'fullname', 'rank',
                     'first_name', 'last_name', 'middle_name', 'suffix')

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
                    writer.writerow(row)

SRC = "cwsac.json"
with open(SRC, 'r') as f:
    data = json.load(f)

battle_csv(data, 'cwsac_battles.csv')
forces_csv(data, 'cwsac_forces.csv')
commanders_csv(data, 'cwsac_commanders.csv')
