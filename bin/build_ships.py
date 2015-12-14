#!/usr/bin/env python
import shutil
from os import path
import sys
import csv

import yaml

FILES = ('ships.csv',)

def build_ships_in_battles(miscdir, dst):
    filename = path.join(miscdir, "ships_in_battles.yaml")
    with open(filename, "r") as f:
        data = yaml.load(f)
    ships = []
    for battle in data:
        for belligerent in ('Confederate', 'US'):
            try:
                for ship in battle[belligerent]:
                    ships.append({'cwsac_id': battle['cwsac_id'],
                                  'belligerent': belligerent,
                                  'ship': ship})
            except KeyError:
                pass
    dstfile = path.join(dst, 'ships_in_battles.csv')
    with open(dstfile, 'w') as f:
        print("Writing %s" % dstfile)
        fieldnames = ('cwsac_id', 'belligerent', 'ship')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(ships)

def copyfiles(miscdir, dst):
    for fn in FILES:
        srcfile = path.join(miscdir, fn)
        dstfile = path.join(dst, fn)
        print("Writing %s" % dstfile)
        shutil.copy(srcfile, dstfile)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    miscdir = path.join(src , 'rawdata' , 'misc')
    copyfiles(miscdir, dst)
    build_ships_in_battles(miscdir, dst)
    
if __name__ == '__main__':
    main()
