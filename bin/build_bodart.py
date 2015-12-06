""" Create csv files from bodart1908/battles.py """
import csv
import os.path
import sys
import shutil

import nameparser
import yaml

RANKS = {"Gen.-Lt." : "Lt. Gen", # "General-Leutnant",
         "Gen." : "Gen.", # "General",
         "GM." : "Maj. Gen.", # "General-Major",
         "Adm." : "Adm.", # "Admiral",
         "GL." : "Lt. Gen.", # "General-Leutnant",
         "BM." : "Brig. Gen.", # "Brigade-General",
         "Brig.-Gen." : "Brig. Gen.", # "Brigade-General",
         "Oberst" : "Col.", # "Oberst",
         "B.-G." : "Brig. Gen.", # "Brigade-General",
         "Brig. Gen." : "Brig. Gen.", # "Brigade-General",
         "komm. Gen." : "Gen.", # "General",
         "Brig-Gen." : "Brig. Gen.", # Brigade-General",
         "G.-L." : "Lt. Gen.", # "General-Leutnant",
         "Brigadier Obst." : "Col.", # Brigadier Oberst" 
}

CATEGORIES = ("battle", "meeting", "surrender",
              "siege", "capture")

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

fields_forces = (
    "battle_id",
    "country",
    "victor",
    "strength",
    "strength_engaged",
    "infantry",
    "cavalry",
    "artillery",
    "guns",
    "killed",
    "killed_percent",    
    "killed_generals",
    "killed_officers",
    "killed_wounded",
    "killed_wounded_percent",
    "killed_wounded_generals",
    "killed_wounded_officers",
    "wounded",
    "wounded_percent",
    "wounded_generals",
    "wounded_officers",
    "captured",
    "captured_generals",
    "captured_officers",
    "missing",
    "missing_percent",
    "missing_generals",
    "missing_officers",
    "casualties",
    "casualties_percent",
    "casualties_officers",
    "casualties_generals",
    "losses_guns",
    "losses_caissons",
    "losses_cannon",
    "losses_canons",
    "losses_flags",
    "losses_munition_wagons",
    "losses_wagons",
    "other"
)

def forces_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    # Get fieldnames
    # fieldnames = set()
    # for battle, v in sorted(data.items()):
    #     for force in ('victor', 'loser'):
    #         for field, v2 in sorted(v[force].items()):
    #             fieldnames.add(field)
    fieldnames = fields_forces
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle, v in sorted(data.items()):
                for side in ('victor', 'loser'):
                    row = dict_subset(v[side], fieldnames)
                    row['victor'] = (side == 'victor')
                    row['battle_id'] = battle
                    writer.writerow(row)

def commanders_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle_id',
                  'country',
                  'name',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'suffix',
                  'rank',
                  'dbpedia')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle, v in sorted(data.items()):
                for side in ('victor', 'loser'):
                    if 'commanders' in v[side]:
                      cmdrs = v[side]['commanders']
                      for cmdr in cmdrs:
                          row = cmdr.copy()
                          row['battle_id'] = battle
                          row['country'] = v[side]['country']
                          row['rank'] = RANKS[row['rank']]
                          if 'dbpedia' not in row:
                              row['dbpedia'] = None
                          writer.writerow(row)

def generals_killed_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle_id',
                  'country',
                  'name',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'suffix',
                  'rank', 
                  'date',
                  'dbpedia')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle, v in sorted(data.items()):
                for side in ('victor', 'loser'):
                    if 'generals_killed' in v[side]:
                        for x in v[side]['generals_killed']:
                            row = x.copy()
                            parsed_name = nameparser.HumanName(row['name']).as_dict()
                            if parsed_name['last'] == '':
                                row['first_name'] = ''
                                row['last_name'] = parsed_name['first']
                            else:
                                row['first_name'] = parsed_name['first']
                                row['last_name'] = parsed_name['last']
                            row['middle_name'] = parsed_name['middle']
                            row['suffix'] = parsed_name['suffix']
                            row['battle_id'] = battle
                            row['country'] = v[side]['country']
                            row['rank'] = RANKS[row['rank']]
                            if 'dbpedia' not in row:
                                row['dbpedia'] = None
                            writer.writerow(row)
                    
def battle_csv(src, dst):
    fields = [
        'battle_id',
        'name', 
        'other_name', 
        'start_date',
        'end_date',
        'location',
        'order', 
        'siege',
        'battle',
        'meeting',
        'surrender',
        'siege',
        'capture',
        'page']
    with open(src, 'r') as f:
        data = yaml.load(f)
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for battle, v in sorted(data.items()):
            row = dict_subset(v, fields + ['category'])
            if 'other_name' in row:
                if len(row['other_name']):
                    row['other_name'] = ';'.join(row['other_name'])
                else:
                    del row['other_name']
            row['battle_id'] = battle
            if 'category' in row:
                if len(row['category']):
                    for category in CATEGORIES:
                        row[category] = int(category in row['category'])
                del row['category']
            writer.writerow(row)

def bodart_to_cwsac(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('from', 'to', 'relation')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle, v in data.items():
            if 'cwsac' in v:
                for link in v['cwsac']:
                    row = {'from': battle,
                           'to': link['uri'],
                           'relation': link['relation']}
                    writer.writerow(row)
                

def bodart_to_dbpedia(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('from', 'to', 'relation')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle, v in data.items():
            if 'dbpedia' in v:
                for link in v['dbpedia']:
                    row = {'from': battle,
                           'to': link['uri'],
                           'relation': link['relation']}
                    writer.writerow(row)

def build(src, dst):
    filename = os.path.join(src, "bodart.yaml")
    battle_csv(filename, os.path.join(dst, "bodart1908_battles.csv"))
    forces_csv(filename, os.path.join(dst, "bodart1908_forces.csv"))
    commanders_csv(filename, os.path.join(dst, "bodart1908_commanders.csv"))
    generals_killed_csv(filename, os.path.join(dst, "bodart1908_generals_killed.csv"))
    bodart_to_cwsac(filename, os.path.join(dst, "bodart1908_to_dbpedia.csv"))
    bodart_to_dbpedia(filename, os.path.join(dst, "bodart1908_to_cwsac.csv"))

    
def main():
    src, dst = sys.argv[1:3]
    build(src, dst)
    
if __name__ == "__main__":
    main()
