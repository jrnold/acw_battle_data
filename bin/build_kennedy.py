""" Create csv files from bodart1908/battles.py """
import csv
import os.path
import sys
import shutil

import nameparser
import yaml


CATEGORIES = ("battle", "meeting", "surrender",
              "siege", "capture")

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

def forces_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle',
                  'belligerent',
                  'casualties_min',
                  'casualties_max',
                  'killed_wounded_min',
                  'killed_wounded_max',
                  'missing')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle, v in sorted(data.items()):
            print(battle)
            for belligerent in v['forces']:
                row = v['forces'][belligerent]
                row['belligerent'] = belligerent
                row['battle'] = battle
                writer.writerow(row)

def battles_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle',
                  'name',
                  'state',
                  'county',
                  'start_date',
                  'end_date',
                  'casualties_min',
                  'casualties_max',
                  'casualties_text',
                  'missing')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle, v in sorted(data.items()):
            row = v
            row['battle'] = battle
            row = dict_subset(row, fieldnames)
            writer.writerow(row)

def build(src, dst):
    filename = os.path.join(src, "rawdata", "kennedy1997", "kennedy1997.yaml")
    battles_csv(filename, os.path.join(dst, "kennedy1997_battles.csv"))
    forces_csv(filename, os.path.join(dst, "kennedy1997_forces.csv"))
    
def main():
    src, dst = sys.argv[1:3]
    build(src, dst)
    
if __name__ == "__main__":
    main()
