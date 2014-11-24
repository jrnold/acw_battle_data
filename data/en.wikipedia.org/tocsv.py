import csv

import yaml

BATTLE_FIELDS = (
    'battle',
    'id',
    'strength',
    'casualties',
    'notes'
)

FORCES_FIELDS = (
    'battle',
    'belligerent',
    'strength',
    'brigades',
    'companies',
    'divisions',
    'armies',
    'corps',
    'regiments',

    'cavalry_companies',
    'cavalry_brigades',
    'cavalry_corps',
    'cavalry_divisions',
    'cavalry_regiments',

    'artillery_sections',
    'artillery_battalions',
    'artillery_batteries',
    'artillery_companies',
    'artillery_regiments', 
    'artillery_brigade',

    'guns',

    'ships',
    'ironclads',
    'monitors',
    'wooden_warships',
    'ships_misc',
    'rams',
    'transports',
    'gunboats',

    'casualties',
    'killed',
    'wounded',
    'missing',
    'captured',
    'killed_wounded',
    'wounded_missing',
    'captured_missing',

    'losses_guns',
    'losses_ships',
    'losses_trains',
    'losses_wagons',

)

def force_keys():
    keys = set()
    for battle, battledata in sorted(data.items()):
        for force, forcedata in (battledata['belligerents'].items()):
            for k in forcedata:
                keys.add(k)
    print(keys)

def battle_keys(data):
   keys = set()
   for battle, battledata in sorted(data.items()):
       for k in battledata:
           keys.add(k)
   print(keys)


def forces_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, FORCES_FIELDS)
        writer.writeheader()
        for battle, battledata in sorted(data.items()):
            for force, forcedata in (battledata['belligerents'].items()):
                row = forcedata.copy()
                row['battle'] = battle
                row['belligerent'] = force
                writer.writerow(row)

def battles_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, BATTLE_FIELDS)
        writer.writeheader()
        for battle, battledata in sorted(data.items()):
            row = battledata.copy()
            row['battle'] = battle
            del row['belligerents']
            writer.writerow(row)

SRC = "wiki_casualties.yaml"
with open(SRC, "r") as f:
    data = yaml.load(f)
battles_csv(data, "wiki_battles.csv")
forces_csv(data, "wiki_forces.csv")
