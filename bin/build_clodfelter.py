#!/usr/bin/env python3
""" create csv tables from clodfelter.yaml """
import csv
import re
import shutil
import sys
import subprocess as sp
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
    with open(path.join(dst, filename), 'w') as f:
        fieldnames = ('battle', 'theater', 'start_date', 'end_date', 'page')
        writer = csv.DictWriter(f, fieldnames, extrasaction = 'ignore')
        writer.writeheader()
        for i, battle in enumerate(data):
            if 'end_date' not in battle:
                battle['end_date'] = battle['start_date']
            battle['number'] = i
            writer.writerow(battle)

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
    with open(path.join(dst, filename), 'w') as f:
        fieldnames = ['battle', 'belligerent'] + list(fields)
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle in battles:
            for belligerent in battle['forces']:
                row = battle['forces'][belligerent].copy()
                row['battle'] = battle['battle']
                row['belligerent'] = belligerent
                # fix keys with spaces in them
                for k in row:
                    if ' ' in k:
                        row[re.sub(' ', '_', k)] = row[k]
                        del row[k]
                writer.writerow(row)

def cwsac_links(data, dst, filename):
    with open(path.join(dst, filename), 'w') as f:
        fieldnames = ('from', 'to', 'relation')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle in battles:
            if 'cwsac' in battle:
                for link in battle['cwsac']:
                    row = {'from': battle['battle'],
                           'to': link['id'],
                           'relation': link['relation']}
                    writer.writerow(row)

def dbpedia_links(data, dst, filename):
    with open(path.join(dst, filename), 'w') as f:
        fieldnames = ('from', 'to', 'relation')
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle in battles:
            if 'dbpedia' in battle:
                for link in battle['dbpedia']:
                    row = {'from': battle['battle'],
                           'to': link['url'],
                           'relation': link['relation']}
                    writer.writerow(row)

def build(src, dst):
    srcfile = path.join(src, "rawdata", "clodfelter2008",  'clodfelter.yaml')
    with open(srcfile, 'r') as f:
        data = yaml.load(f)

    battles(data, dst, 'clodfelter_battles.csv')
    forces(data, dst, 'clodfelter_forces.csv')
    cwsac_links(data, dst, 'clodfelter_to_cwsac.csv')
    dbpedia_links(data, dst, 'clodfelter_to_dbpedia.csv')

def main():
    build(*sys.argv[1:3])

if __name__ == "__main__":
    main()
    
