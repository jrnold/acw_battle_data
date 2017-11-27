"""Construct battlemisc.csv from the its YAML sources."""
import sys
import os.path
import os
import csv

import yaml


def extract_ships(src):
    """Extract ship data from a battlemisc file."""
    with open(src, "r") as fp:
        data = yaml.load(fp)
    try:
        ships = data['ships']
    except KeyError:
        raise StopIteration()
    for belligerent in ('Confederate', 'US'):
        try:
            for ship in ships[belligerent]:
                yield {
                    'cwsac_id': data['cwsac_id'],
                    'belligerent': belligerent,
                    'ship': ship
                }
        except KeyError:
            pass


def build_ships_in_battles(src, dst):
    """Write csv file with ships in each battle."""
    fieldnames = ('cwsac_id', 'belligerent', 'ship')
    with open(dst, 'w') as fp:
        writer = csv.DictWriter(fp, fieldnames)
        writer.writeheader()
        for filename in os.listdir(src):
            if filename.endswith(".yml"):
                for row in extract_ships(os.path.join(src, filename)):
                    writer.writerow(row)


def process_battlemisc_file(filename):
    """For a battle's YAML file and return only relevant info."""
    with open(filename, 'r') as fp:
        x = yaml.load(fp)
    naval = x.get('naval', 'No')
    data = {
        'cwsac_id': x['cwsac_id'],
        'attacker': x.get('attacker', None),
        'siege': x.get('siege', '0'),
        'naval': naval if naval != "NA" else "No"
    }
    if 'ships' in x:
        for i, k in (('U', 'US'), ('C', 'Confederate')):
            data[f'ships_{i}'] = len(x['ships'].get(k, []))
    else:
        for i in ('U', 'C'):
            data[f'ships_{i}'] = '0'
    return data


def build(src, dst):
    """Process all YAML files and output battlemisc.csv in dst."""
    FIELDS = ('cwsac_id', 'attacker', 'naval', 'siege', 'ships_U', 'ships_C')
    with open(dst, 'w') as fp:
        writer = csv.DictWriter(fp, FIELDS)
        writer.writeheader()
        for filename in os.listdir(src):
            if filename.endswith(".yml"):
                newdata = process_battlemisc_file(os.path.join(src, filename))
                writer.writerow(newdata)


def main():
    """Command line interface."""
    src, dst = sys.argv[1:3]
    srcdir = os.path.join(src, 'rawdata', 'battlemisc', 'battles')
    build(srcdir, os.path.join(dst, 'battlemisc.csv'))
    build_ships_in_battles(srcdir, os.path.join(dst, 'ships_in_battles.csv'))


if __name__ == '__main__':
    main()
