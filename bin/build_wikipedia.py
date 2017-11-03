#!/usr/bin/env python3
import csv
import shutil
import sys
from os import path

import yaml

BATTLE_FIELDS = ('battle_id', 'id', 'cwsac_id')

FORCES_FIELDS = ('battle_id', 'belligerent', 'strength_min', 'strength_max',
                 'casualties_min', 'casualties_max', 'killed_min',
                 'killed_max', 'wounded_min', 'wounded_max', 'missing_min',
                 'missing_max', 'captured_min', 'captured_max',
                 'killed_wounded_min', 'killed_wounded_max',
                 'wounded_missing_min', 'wounded_missing_max',
                 'captured_missing_min', 'captured_missing_max')


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
    """If only one key given, make min and max kays."""
    if k in x:
        if x[k]:
            x['%s_min' % k] = x['%s_max' % k] = x[k]
        del x[k]


def forces_csv(data, filename):
    with open(filename, 'w', encoding="utf8") as f:
        writer = csv.DictWriter(f, FORCES_FIELDS, extrasaction='ignore')
        writer.writeheader()
        for battle, battledata in sorted(data.items()):
            for force, forcedata in (battledata['belligerents'].items()):
                row = forcedata.copy()
                row['battle_id'] = battle
                if force == 'US':
                    row['belligerent'] = 'US'
                elif force == 'CS':
                    row['belligerent'] = 'Confederate'
                elif force == 'I':
                    row['belligerent'] = 'Native American'
                else:
                    raise Exception('%s is not a valid belligerent' % force)
                for k in ('strength', 'casualties', 'killed', 'wounded',
                          'missing', 'captured', 'killed_wounded',
                          'wounded_missing', 'captured_missing'):
                    var_to_range(row, k)
                writer.writerow(row)


def battles_csv(data, filename):
    with open(filename, 'w', encoding="utf8") as f:
        writer = csv.DictWriter(f, BATTLE_FIELDS, extrasaction='ignore')
        writer.writeheader()
        for battle, battledata in sorted(data.items()):
            row = battledata.copy()
            row['battle_id'] = battle
            del row['belligerents']
            writer.writerow(row)


def build(src, dst):
    srcdir = path.join(src, "rawdata", "en.wikipedia.org")
    with open(
            path.join(srcdir, 'wikipedia_casualties.yaml'), 'r',
            encoding="utf8") as f:
        data = yaml.load(f)
    battles_csv(data, path.join(dst, 'wikipedia_battles.csv'))
    forces_csv(data, path.join(dst, 'wikipedia_forces.csv'))


def main():
    src, dst = sys.argv[1:3]
    build(src, dst)


if __name__ == "__main__":
    main()
