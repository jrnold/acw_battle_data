""" Create csv files from bodart1908/battles.py """
import csv
import os.path
import sys

import yaml

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

def forces_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    # Get fieldnames
    fieldnames = set()
    for battle, v in data.items():
        for force in ('victor', 'loser'):
            for field, v2 in v[force].items():
                fieldnames.add(field)
    fieldnames -= {'commander', 'generals_killed'}
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, ['battle', 'victor'] + list(fieldnames))
        with open(dst, 'w') as f:
            for battle, v in data.items():
                for side in ('victor', 'loser'):
                    row = dict_subset(v[side], fieldnames)
                    row['victor'] = side == 'victor'
                    row['battle'] = battle
                    writer.writerow(row)

def commanders_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle',
                  'country',
                  'name',
                  'rank')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        with open(dst, 'w') as f:
            for battle, v in data.items():
                for side in ('victor', 'loser'):
                    if 'commander' in v[side]:
                      cmdrs = v[side]['commander']
                      if not isinstance(cmdrs, list):
                          cmdrs = [cmdrs]
                      for cmdr in cmdrs:
                          row = cmdr.copy()
                          row['battle'] = battle
                          row['country'] = v[side]['country']
                          writer.writerow(row)

def generals_killed_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle',
                  'country',
                  'name',
                  'rank', 'date')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        with open(dst, 'w') as f:
            for battle, v in data.items():
                for side in ('victor', 'loser'):
                    if 'generals_killed' in v[side]:
                        for x in v[side]['generals_killed']:
                            row = x.copy()
                            row['battle'] = battle
                            row['country'] = v[side]['country']
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
        for battle, v in data.items():
            row = dict_subset(v, fields)
            if 'other_name' in row and row['other_name']:
                row['other_name'] = ';'.join(row['other_name'])
            row['category'] = ';'.join(row['category'])
            writer.writerow(row)

def main():
    filename = sys.argv[1]
    dst_dir = sys.argv[2]
    battle_csv(filename, os.path.join(dst_dir, 'bodart_battles.csv'))
    forces_csv(filename, os.path.join(dst_dir, 'bodart_forces.csv'))
    commanders_csv(filename, os.path.join(dst_dir, 'bodart_commanders.csv'))
    generals_killed_csv(filename, os.path.join(dst_dir, 'bodart_generals_killed.csv'))

if __name__ == "__main__":
    main()
