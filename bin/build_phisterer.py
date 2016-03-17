# -*- coding: utf-8 -*-
import re
import sys
import calendar
import csv
import json
import sys
import shutil
from os import path

import yaml

_PHISTERER_DIR = ('rawdata', 'phisterer1883')

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

def build_losses(src, dst):
    with open(path.join(src, *_PHISTERER_DIR, 'phisterer_losses.csv'), 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        data = [row for row in reader]
    with open(path.join(dst, 'phisterer_battles.csv'), 'w') as f:
        fieldnames = ('battle_id', 'battle_name', 'state', 'start_date', 'end_date', 'surrender', 'campaign', 'page')
        writer = csv.DictWriter(f, fieldnames, extrasaction = 'ignore')
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    with open(path.join(dst, 'phisterer_forces.csv'), 'w') as f:
        fieldnames = ('battle_id', 'belligerent', 'casualties', 'killed', 'wounded', 'missing')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for row in data:
            cs = {'battle_id': row['battle_id'],
                  'belligerent': 'Confederate',
                  'casualties': row['cs_losses']}
            writer.writerow(cs)
            us = {'battle_id': row['battle_id'],
                  'belligerent': 'US',
                  'casualties': row['us_losses'],
                  'killed': row['us_killed'],
                  'wounded': row['us_wounded'],
                  'missing': row['us_missing']}
            writer.writerow(us)

def build_to_cwsac(src, dst):
    srcfile = path.join(src, *_PHISTERER_DIR, 'phisterer_to_cwsac.yaml')
    dstfile = path.join(dst, 'phisterer_to_cwsac.json')
    with open(srcfile, 'r') as f:
        data = yaml.load(f)
    ret = []
    for row in data:
        newrow = {'relation': row['relation']}
        newrow['battles_to'] = [x['id'] for x in row['battles_cwsac']]
        newrow['battles_from'] = [x['id'] for x in row['battles_from']]
        ret.append(newrow)
    with open(dstfile, 'w') as f:
        json.dump(ret, f)

def copyfiles(src, dst):
    filelist = ("phisterer_engagements_by_year.csv",
                "phisterer_engagements.csv")
    for filename in filelist:
        shutil.copy(path.join(src, 'rawdata', 'phisterer1883', filename), dst)

def build(src, dst):
    build_losses(src, dst)
    build_to_cwsac(src, dst)
    copyfiles(src, dst)

def main():
    build(*sys.argv[1:3])

if __name__ == "__main__":
    main()
