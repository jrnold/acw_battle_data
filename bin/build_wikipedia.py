#!/usr/bin/env python3
import csv
import sys
import shutil
from os import path

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
    'strength_min',
    'strength_max',
    'casualties_min',
    'casualties_max',
    'killed_min',
    'killed_max',
    'wounded_min',
    'wounded_max',
    'missing_min',
    'missing_max',
    'captured_min',
    'captured_max',
    'killed_wounded_min',
    'killed_wounded_max',
    'wounded_missing_min',
    'wounded_missing_max',
    'captured_missing_min',
    'captured_missing_max'
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

def var_to_range(x, k):
    if k in x:
        if x[k]:
            xk = str(x[k]).split('-')
            if len(xk) > 1:
                x['%s_min' % k ] = xk[0]
                x['%s_max' % k ] = xk[1]
            else:
                x['%s_min' % k] = x['%s_max' % k] = x[k]
        del x[k]

def forces_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, FORCES_FIELDS)
        writer.writeheader()
        for battle, battledata in sorted(data.items()):
            for force, forcedata in (battledata['belligerents'].items()):
                row = forcedata.copy()
                row['battle'] = battle
                row['belligerent'] = force
                for k in ('strength', 'casualties', 'killed', 'wounded', 'missing',
                          'captured', 'killed_wounded', 'wounded_missing',
                          'captured_missing'):
                    var_to_range(row, k)
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

def tocsv(src, dst):
    srcfile = path.join(src, "wiki_casualties.yaml")
    with open(srcfile, "r") as f:
        data = yaml.load(f)
    battles_csv(data, path.join(dst, "wikipedia_battles.csv"))
    forces_csv(data, path.join(dst, "wikipedia_forces.csv"))

def copyfiles(src, dst):
    shutil.copy(path.join(src, "wikipedia_to_cwsac.csv"), dst)

def build(src, dst):
    srcdir = path.join(src, "rawdata", "en.wikipedia.org")
    tocsv(srcdir, dst)
    copyfiles(srcdir, dst)

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()