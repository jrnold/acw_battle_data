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
          'battle',
          'strength',
          'campaign',
          'results_text',
          'significance',
          'results',
          'uri',
          # 'combatants',
          'preservation',
          'forces_text',
          'casualties',
          'principal_commanders',
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
        for battle, battle_data in data.items():
            row = dict_subset(battle_data, battle_fields)
            writer.writerow(row)

combatant_fields = ('battle',
 'combatant',
 'corps',
 'strength',
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
 'strength_min',
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
 'strength_max')

def combatants_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, combatant_fields)
        writer.writeheader()
        for battle, battle_data in data.items():
            for combatant, x in battle_data['combatants'].items():
                row = dict_subset(battle_data, combatant_fields)
                row['battle'] = battle
                row['combatant'] = combatant
                writer.writerow(row)

commanders_fields = ('battle', 'combatant', 'fullname', 'rank')

def commanders_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, commanders_fields)
        writer.writeheader()
        for battle, battle_data in data.items():
            for combatant, x in battle_data['combatants'].items():
                for commander in x['commanders']:
                    row = commander.copy()
                    row['battle'] = battle
                    row['combatant'] = combatant
                    writer.writerow(row)

SRC = "cwsac.json"
with open(SRC, 'r') as f:
    data = json.load(f)

battle_csv(data, 'cwsac_battles.csv')
combatants_csv(data, 'cwsac_comabatants.csv')
commanders_csv(data, 'cwsac_commanders.csv')
