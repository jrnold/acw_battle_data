# -*- coding: utf-8 -*-
import re
import sys
import calendar
import csv
import sys
import shutil
from os import path

import yaml

def build_losses(src, dst):
    with open(path.join(src, 'phisterer_losses.csv'), 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        data = [row for row in reader]
    with open(path.join(src, 'misc.yaml'), 'r') as f:
        miscdata = yaml.load(f)
    with open(path.join(dst, 'phisterer_losses.csv'), 'w') as f:
        writer = csv.DictWriter(f, list(fieldnames) + ['campaign', 'surrender'])
        writer.writeheader()
        for row in data:
            row['campaign'] = int(row['battle'] in miscdata['campaigns'])
            row['surrender'] = int(row['battle'] in miscdata['surrenders'])
            writer.writerow(row)

def copyfiles(src, dst):
    filelist = ("phisterer_engagements_by_year.csv", "phisterer_engagements.csv",
                 "phisterer_to_cwsac.csv", "phisterer_to_dbpedia.csv")
    for filename in filelist:
        shutil.copy(path.join(src, filename), dst)

def build(src, dst):
    build_losses(src, dst)
    copyfiles(src, dst)

def main():
    build(*sys.argv[1:3])

if __name__ == "__main__":
    main()
