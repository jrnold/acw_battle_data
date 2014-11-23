""" Create csv files from bodart1908/battles.py """
import csv
import os.path
import sys

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


def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

fields_forces = (
    "battle",
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
        writer = csv.DictWriter(f, ['battle', 'victor'] + list(fieldnames))
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle, v in sorted(data.items()):
                for side in ('victor', 'loser'):
                    row = dict_subset(v[side], fieldnames)
                    row['victor'] = (side == 'victor')
                    row['battle'] = battle
                    writer.writerow(row)

def commanders_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle',
                  'country',
                  'name',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'suffix',
                  'rank')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle, v in sorted(data.items()):
                for side in ('victor', 'loser'):
                    if 'commander' in v[side]:
                      cmdrs = v[side]['commander']
                      if not isinstance(cmdrs, list):
                          cmdrs = [cmdrs]
                      for cmdr in cmdrs:
                          row = cmdr.copy()
                          parsed_name = nameparser.HumanName(row['name']).as_dict()
                          # if only one name given, it is treated as a first name
                          if parsed_name['last'] == '':
                              row['first_name'] = ''
                              row['last_name'] = parsed_name['first']
                          else:
                              row['first_name'] = parsed_name['first']
                              row['last_name'] = parsed_name['last']
                          row['middle_name'] = parsed_name['middle']
                          row['suffix'] = parsed_name['suffix']
                          row['battle'] = battle
                          row['country'] = v[side]['country']
                          row['rank'] = RANKS[row['rank']]
                          writer.writerow(row)

def generals_killed_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle',
                  'country',
                  'name',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'suffix',
                  'rank', 
                  'date')
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
                            row['battle'] = battle
                            row['country'] = v[side]['country']
                            row['rank'] = RANKS[row['rank']]
                            writer.writerow(row)
                    
def battle_csv(src, dst):
    fields = (
        'name', 
        'other_name', 
        'start_date',
        'end_date',
        'location',
        'category',
        'order', 
        'page')
    with open(src, 'r') as f:
        data = yaml.load(f)
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for battle, v in sorted(data.items()):
            row = dict_subset(v, fields)
            if 'other_name' in row:
                if len(row['other_name']):
                    row['other_name'] = ';'.join(row['other_name'])
                else:
                    del row['other_name']
            row['category'] = ';'.join(row['category'])
            writer.writerow(row)

def main():
    filename = "bodart.yaml" #sys.argv[1]
    dst_dir = "." # sys.argv[2]
    battle_csv(filename, os.path.join(dst_dir, "bodart_battles.csv"))
    forces_csv(filename, os.path.join(dst_dir, "bodart_forces.csv"))
    commanders_csv(filename, os.path.join(dst_dir, "bodart_commanders.csv"))
    generals_killed_csv(filename, os.path.join(dst_dir, "bodart_generals_killed.csv"))

if __name__ == "__main__":
    main()
