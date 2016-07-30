#!/usr/bin/env python3
""" create csv tables from clodfelter.yaml """
import csv
import json
import re
import shutil
import subprocess as sp
import sys
from os import path

import yaml

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

def rename(x, k, j):
    if k in x:
        x[j] = x[k]
        del x[k]

def battles(data, dst, filename):
    with open(path.join(dst, filename), 'w', encoding='utf8') as f:
        fieldnames = ('battle_id', 'theater', 'theater_years', 'start_date', 'end_date', 'result', 'page')
        writer = csv.DictWriter(f, fieldnames, extrasaction = 'ignore')
        writer.writeheader()
        for i, battle in enumerate(data):
            if 'end_date' not in battle:
                battle['end_date'] = battle['start_date']
            battle['theater_years'] = battle['theater']
            if re.search("East", battle['theater_years']):
                battle['theater'] = "Eastern"
            if re.search("West", battle['theater_years']):
                battle['theater'] = "Western"
            if re.search("Blockade", battle['theater_years']):
                battle['theater'] = "Blockade"
            battle['number'] = i
            writer.writerow(battle)

def commanders(data, dst, filename):
    with open(path.join(dst, filename), 'w', encoding='utf8') as f:
        fieldnames = ('battle_id', 'belligerent', 'commander_number',
                      'PersonID', 'last_name', 'first_name', 'middle_name', 'middle_initial', 'rank', 'navy')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for i, battle in enumerate(data):
            for belligerent in battle['forces']:
                force = battle['forces'][belligerent]
                for j, cdr in enumerate(force['commanders']):
                    cdr['battle_id'] = battle['battle_id']
                    cdr['belligerent'] = belligerent
                    cdr['commander_number'] = j
                    writer.writerow(cdr)

def forces(data, dst, filename):
    fields = (
    'strength',
    'infantry',
    'cavalry',
    'crewmen',
    # units
    'corps',
    'cavalry_corps',
    'divisions',
    'cavalry_divisions',
    'brigades',
    'companies',
    # ships
    'frigates',
    'gunboats',
    'ironclads',
    'sloops',
    'steamers',
    'warships_and_transports',
    'warships',
    'wooden_warships',
    # artillery_guns
    'guns',
    # casualties of personnel
    'casualties',
    'captured',
    'killed',
    'wounded',
    'missing',
    'killed_wounded',
    'killed_missing',
    'missing_captured',
    'wounded_missing',
    # casualties of "stuff"
    'guns_lost',
    'guns_captured',
    'small_arms_lost',
    'small_arms_captured',
    'warships_sunk',
    'warships_damaged',
    'gunboats_sunk',
    'gunboats_captured',
    'ironclads_sunk',
    'ironclads_captured',
    'forts_captured',
    # misc
    'note'
    )
    with open(path.join(dst, filename), 'w', encoding='utf8') as f:
        fieldnames = ['battle_id', 'belligerent'] + list(fields)
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for i, battle in enumerate(data):
            for belligerent in battle['forces']:
                row = battle['forces'][belligerent].copy()
                row['battle_id'] = battle['battle_id']
                row['belligerent'] = belligerent
                del row['commanders']
                # fix keys with spaces in them
                writer.writerow(row)

def cwsac_links(src, dst):
    with open(src, 'r', encoding='utf8') as f:
        data = yaml.load(f)
    ret = []
    for x in data:
        toadd = {'relation': x['relation']}
        toadd['battles_from'] = [btl['id'] for btl in x['battles_from']]
        toadd['battles_to'] = [btl['id'] for btl in x['battles_cwsac']]
        ret.append(toadd)
    with open(dst, 'w', encoding='utf8') as f:
        json.dump(ret, f)

def dbpedia_links(src, dst):
    with open(src, 'r', encoding='utf8') as f:
        data = yaml.load(f)
    ret = []
    for x in data:
        toadd = {'relation': x['relation']}
        toadd['battles_from'] = [btl['id'] for btl in x['battles_from']]
        toadd['battles_to'] = x['battles_dbpedia']
        ret.append(toadd)
    with open(dst, 'w', encoding='utf8') as f:
        json.dump(ret, f)

def build(src, dst):
    srcfile = path.join(src, "rawdata", "clodfelter2008",  'clodfelter.yaml')
    with open(srcfile, 'r', encoding='utf8') as f:
        data = yaml.load(f)

    battles(data, dst, 'clodfelter_battles.csv')
    forces(data, dst, 'clodfelter_forces.csv')
    commanders(data, dst, 'clodfelter_commanders.csv')
    cwsac_links(path.join(src, "rawdata", "clodfelter2008", 'clodfelter_to_cwsac.yaml'),
                path.join(dst, 'clodfelter_to_cwsac.json'))
    dbpedia_links(path.join(src, "rawdata", "clodfelter2008", 'clodfelter_to_dbpedia.yaml'),
                path.join(dst, 'clodfelter_to_dbpedia.json'))

def main():
    build(*sys.argv[1:3])

if __name__ == "__main__":
    main()
