# -*- coding: utf-8 -*-
import re
import sys
import calendar
import csv
import sys
import shutil
from os import path

import yaml

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

def build_losses(src, dst):
    with open(path.join(src, 'rawdata', 'phisterer1883', 'phisterer_losses.csv'), 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        data = [row for row in reader]
    with open(path.join(dst, 'phisterer_battles.csv'), 'w') as f:
        fieldnames = ('battle', 'battle_name', 'state', 'start_date', 'end_date', 'surrender', 'campaign', 'page')
        writer = csv.DictWriter(f, fieldnames, extrasaction = 'ignore')
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    with open(path.join(dst, 'phisterer_forces.csv'), 'w') as f:
        fieldnames = ('battle', 'belligerent', 'casualties', 'killed', 'wounded', 'missing')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for row in data:
            cs = {'battle': row['battle'],
                  'belligerent': 'Confederate',
                  'casualties': row['cs_losses']}
            writer.writerow(cs)            
            us = {'battle': row['battle'],
                  'belligerent': 'US',
                  'casualties': row['us_losses'],
                  'killed': row['us_killed'],
                  'wounded': row['us_wounded'],
                  'missing': row['us_missing']}
            writer.writerow(us)
    

def copyfiles(src, dst):
    filelist = ("phisterer_engagements_by_year.csv",
                "phisterer_engagements.csv",
                 "phisterer_to_cwsac.csv",
                "phisterer_to_dbpedia.csv")
    for filename in filelist:
        shutil.copy(path.join(src, 'rawdata', 'phisterer1883', filename), dst)

def build(src, dst):
    build_losses(src, dst)
    copyfiles(src, dst)

def main():
    build(*sys.argv[1:3])

if __name__ == "__main__":
    main()
