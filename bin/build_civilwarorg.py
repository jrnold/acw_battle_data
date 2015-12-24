""" Convert cwsac.json to csv files """
import json
import csv
import sys
import shutil
from os import path

def build_forces(data, dst):
    fields = ('id',
              'belligerent',
              'strength',
              'casualties',
              'killed',
              'wounded',
              'missing_captured')
    forces = []
    for battle in data:
        union = {'id': battle['id'], 'belligerent': 'US'}
        union['casualties'] = battle['union_casualties'] if 'union_casualties' in battle else None
        union['strength'] = battle['union_strength'] if 'union_strength' in battle else None
        union['killed'] = battle['union_killed'] if 'union_killed' in battle else None
        union['wounded'] = battle['union_wounded'] if 'union_wounded' in battle else None
        forces.append(union)
        confederate = {'id': battle['id'], 'belligerent': 'Commanders'}
        confederate['casualties'] = battle['confederate_casualties'] if 'confederate_casualties' in battle else None
        confederate['strength'] = battle['confederate_strength'] if 'confederate_strength' in battle else None
        confederate['killed'] = battle['confederate_killed'] if 'confederate_killed' in battle else None
        confederate['wounded'] = battle['confederate_wounded'] if 'confederate_wounded' in battle else None
        forces.append(confederate)

    with open(dst, 'w') as f:
        print("Writing: %s" % dst)
        writer = csv.DictWriter(f, fields, extrasaction = 'raise')
        writer.writeheader()
        writer.writerows(forces)

def build_commanders(data, dst):
    fields = ('id',
              'belligerent',
              'name',
              'url')
    commanders = []
    for battle in data:
        for cdr in battle['union_commanders']:
            commanders.append({'id': battle['id'], 'belligerent': 'US',
                               'name': cdr['name'], 'url': cdr['url']})
        for cdr in battle['confederate_commanders']:
            commanders.append({'id': battle['id'], 'belligerent': 'Confederate',
                               'name': cdr['name'], 'url': cdr['url']})
    with open(dst, 'w') as f:
        print("Writing: %s" % dst)        
        writer = csv.DictWriter(f, fields, extrasaction = 'raise')
        writer.writeheader()
        writer.writerows(commanders)
        

def build_battles(data, dst):
    fields = ('id',
              'name',
              'url',
              'dates',
              'alternate_names',
              'location',
              'campaign',              
              'result',
              'total_casualties',
              'total_strength')
    with open(dst, 'w') as f:
        print("Writing: %s" % dst)
        writer = csv.DictWriter(f, fields, extrasaction = 'ignore')
        writer.writeheader()
        writer.writerows(data)


def build(src, dst):
    srcdir = path.join(src, 'rawdata', 'civilwar.org')
    srcfile = path.join(srcdir, 'civilwar.org.json')
    with open(srcfile, 'r') as f:
        data = json.load(f)
    build_battles(data, path.join(dst, 'civilwarorg_battles.csv'))
    build_forces(data, path.join(dst, 'civilwarorg_forces.csv'))
    build_commanders(data, path.join(dst, 'civilwarorg_commanders.csv'))

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == '__main__':
    main()
