""" Create csv files from bodart1908/battles.py """
import csv
import os.path
import sys

import yaml
import json

CATEGORIES = ("battle", "meeting", "surrender",
              "siege", "capture")

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

def forces_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle_id',
                  'belligerent',
                  'casualties_min',
                  'casualties_max',
                  'killed_wounded_min',
                  'killed_wounded_max',
                  'missing',
                  'aggregate',
                  'battles_aggregated')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle in data:
            if battle['forces']:
                try:
                    battles_aggregated = ' '.join(battle['casualties_battles'])
                    aggregate = 1
                except KeyError:
                    aggregate = 0
                    battles_aggregated = battle
                for belligerent in battle['forces']:
                    row = battle['forces'][belligerent]
                    row['belligerent'] = belligerent
                    row['battle_id'] = battle['battle_id']
                    row['aggregate'] = aggregate
                    row['battles_aggregated'] = battles_aggregated
                    writer.writerow(row)

def battles_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle_id',
                  'battle_name',
                  'state',
                  'county',
                  'start_date',
                  'end_date',
                  'casualties_min',
                  'casualties_max',
                  'casualties_text',
                  'missing',
                  'cwsac_id')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle in data:
            row = battle.copy()
            if 'cwsac_id' not in row:
                battle['cwsac_id'] = battle['battle_id']
            row = dict_subset(row, fieldnames)
            writer.writerow(row)

def forces_to_cwsac(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    ret = []
    for battle in data:
        if battle['forces']:
            try:
                cwsac = battle['casualties_battles']
            except KeyError:
                try:
                    cwsac = [battle['cwsac_id']]
                except KeyError:
                    cwsac = [battle['battle_id']]
            ret.append({'battles_from': [battle['battle_id']],
                         'battles_to': cwsac,
                         'relation': 'eq'})
    with open(dst, 'w') as f:
        json.dump(ret, f)

def build(src, dst):
    filename = os.path.join(src, "rawdata", "kennedy1997", "kennedy1997.yaml")
    battles_csv(filename, os.path.join(dst, "kennedy1997_battles.csv"))
    forces_csv(filename, os.path.join(dst, "kennedy1997_forces.csv"))
    forces_to_cwsac(filename, os.path.join(dst, "kennedy1997_forces_to_cwsac.json"))

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()
