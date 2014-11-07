""" Create csv files from bodart1908/battles.py """
import os.path
import sys

import yaml

def dict_remove(x, exclude = []):
    dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, exclude = []):
    dict((k, v) for k, v in x.items() if k in exclude)

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
                    row = dict_remove(v[side], fieldnames)
                    row['victor'] = side == 'victor'
                    row['battle'] = battle
                    writer.writerow(battle)

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
                    row = v[side]['commander']
                    row['battle'] = battle
                    row['country'] = country
                    writer.writerow(battle)

def generals_killed_csv(src, dst):
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
                    row = v[side]['generals_killed']
                    row['battle'] = battle
                    row['country'] = country
                    writer.writerow(battle)
                    
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
        writer = csv.DictWriter(dst, fields)
        for battle, v in data.items():
            row = dict_subset(v, fieldnames)
            row['other_name'] = ';'.join(row['other_name'])
            row['category'] = ';'.join(row['category'])
            writer.writerow(row)

def main():
    filename = sys.argv[1]
    dst_dir = sys.argv[1]
    battle_csv(filename, os.path.join(dst_dir, 'bodart_battles.csv'))
    # forces_csv(filename, 'bodart_forces.csv')
    # commanders_csv(filename, 'bodart_commanders.csv')
    # generals_killed_csv(filename, 'bodart_generals_killed.csv')

if __name__ == "__main__":
    main()
