#!/usr/bin/env python
import shutil
from os import path
import sys
import csv

import yaml

FILES = ('ships.csv',)

def build_navalbattles(src, dst):
    filename = path.join(src, "rawdata", "ships", "ships_in_battles.yaml")
    with open(filename, "r") as f:
        data = yaml.load(f)
    battles = []
    for battle in data:
        confederate_ships = len(battle['Confederate'])
        us_ships = len(battle['US'])
        us_fortifications = 'US' in battle['fortifications']
        confederate_fortifications = 'Confederate' in battle['fortifications']        
        btl = {'cwsac_id': battle['cwsac_id'],
               'confederate_ships': confederate_ships,
               'us_ships': confederate_ships,
               'confederate_fortifications': confederate_fortifications,
               'us_fortifications': confederate_fortifications}
        battles.append(btl)
    dstfile = path.join(dst, 'navalbattles.csv')
    with open(dstfile, 'w') as f:
        print("Writing: %s" % dstfile)
        fieldnames = ('cwsac_id',
                      'confederate_ships',
                      'us_ships',
                      'confederate_fortifications',
                      'us_fortifications')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(battles)
    

def build_ships_in_battles(src, dst):
    filename = path.join(src, "rawdata", "ships", "ships_in_battles.yaml")
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
        print("Writing: %s" % dstfile)
        fieldnames = ('cwsac_id', 'belligerent', 'ship')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(ships)

def copyfiles(src, dst):
    for fn in FILES:
        srcfile = path.join(src, "rawdata", "ships", fn)
        dstfile = path.join(dst, fn)
        print("Writing: %s" % dstfile)
        shutil.copy(srcfile, dstfile)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    print("Building ships data")
    copyfiles(src, dst)
    build_ships_in_battles(src, dst)
    build_navalbattles(src, dst)    
    
if __name__ == '__main__':
    main()
