""" Convert cwsac.json to csv files """
import csv
import datetime
import json
import re
import sys
from os import path

STATES = {
    "Alabama": "AL",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "Colorado": "CO",
    "District of Columbia": "DC",
    "Florida": "FL",
    "Georgia": "GA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maryland": "MD",
    "Mississippi": "MS",
    "Missouri": "MO",
    "New Mexico": "NM",
    "North Carolina": "NC",
    "Oklahoma": "OK",
    "Pennsylvania": "PA",
    "South Carolina": "SC",
    "Tennessee": "TN",
    "Texas": "TX",
    "Virginia": "VA",
    "West Virginia": "WV"
}

MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

REGEX_DATE = re.compile(''.join(
    ('(?P<m>%s) (?P<d>\d+)', '(?: - (?P<m2>%s)? *(?P<d2>\d+))?',
     ', (?P<year>\d{4})')) % ('|'.join(MONTHS), '|'.join(MONTHS)))


def comma_int(x):
    if x is None or x == '':
        return None
    return int(re.sub(',', '', x))


def get_force(x, belligerent):
    ret = {'battle_id': x['id'], 'belligerent': belligerent}
    prefix = 'union' if belligerent == 'US' else 'confederate'
    for k in ('casualties', 'strength', 'killed', 'wounded',
              'missing_captured'):
        try:
            ret[k] = x[prefix + '_' + k]
        except KeyError:
            ret[k] = None
    if ret['casualties'] and ret['killed'] and ret['wounded'] and ret['missing_captured'] is None:
        ret['casualties'] = None
    if ret['casualties'] and ret['killed'] is None and ret['wounded'] is None and ret['missing_captured']:
        ret['killed_wounded'] = ret['casualties'] - ret['missing_captured']
    elif ret['wounded'] is not None and ret['killed'] is not None:
        ret['killed_wounded'] = ret['killed'] + ret['wounded']
    else:
        ret['killed_wounded'] = None
    return ret


def build_forces(data, dst):
    fields = ('battle_id', 'belligerent', 'strength', 'casualties', 'killed',
              'wounded', 'killed_wounded', 'missing_captured')
    forces = []
    for battle in data:
        forces.append(get_force(battle, 'US'))
        forces.append(get_force(battle, 'Confederate'))
    with open(dst, 'w', encoding='utf8') as f:
        print("Writing: %s" % dst)
        writer = csv.DictWriter(f, fields, extrasaction='raise')
        writer.writeheader()
        writer.writerows(forces)


def build_commanders(data, dst):
    fields = ('battle_id', 'belligerent', 'name', 'url')
    commanders = []
    for battle in data:
        for cdr in battle['union_commanders']:
            commanders.append({
                'battle_id': battle['id'],
                'belligerent': 'US',
                'name': cdr['name'],
                'url': cdr['url']
            })
        for cdr in battle['confederate_commanders']:
            commanders.append({
                'battle_id': battle['id'],
                'belligerent': 'Confederate',
                'name': cdr['name'],
                'url': cdr['url']
            })
    with open(dst, 'w', encoding='utf8') as f:
        print("Writing: %s" % dst)
        writer = csv.DictWriter(f, fields, extrasaction='raise')
        writer.writeheader()
        writer.writerows(commanders)


def build_battles(data, links, dst):
    fields = ('battle_id', 'battle_name', 'url', 'start_date', 'end_date',
              'alternate_names', 'location', 'state', 'campaign', 'result',
              'total_casualties', 'total_strength', 'cwsac_id', 'dbpedia_url')
    with open(dst, 'w', encoding='utf8') as f:
        print("Writing: %s" % dst)
        writer = csv.DictWriter(f, fields, extrasaction='ignore')
        writer.writeheader()
        for row in data:
            m = re.match('^(.*),(.*?)$', row['location'])
            row['location'] = m.group(1).strip()
            row['state'] = STATES[m.group(2).strip()]
            m = REGEX_DATE.match(row['dates'])
            if m:
                year = int(m.group('year'))
                day1 = int(m.group('d'))
                day2 = int(m.group('d2')) if m.group('d2') else day1
                month1 = MONTHS.index(m.group('m')) + 1
                month2 = MONTHS.index(m.group('m2')) + 1 if m.group(
                    'm2') else month1
                row['start_date'] = datetime.date(year, month1, day1)
                if row['id'] == 'stones-river':
                    row['start_date'] = row['start_date'].replace(year=1862)
                row['end_date'] = datetime.date(year, month2, day2)
            else:
                print(row['dates'])
            row['cwsac_id'] = links[row['id']]['cwsac']
            row['dbpedia_url'] = links[row['id']]['dbpedia']
            row['battle_id'] = row['id']
            row['battle_name'] = row['name']
            for k in ('total_casualties', 'total_strength'):
                try:
                    row[k] = comma_int(row[k])
                except KeyError:
                    pass
            writer.writerow(row)


def build(src, dst):
    srcdir = path.join(src, 'rawdata', 'civilwar.org')
    srcfile = path.join(srcdir, 'civilwar.org.json')
    with open(srcfile, 'r', encoding='utf8') as f:
        data = json.load(f)
    with open(path.join(srcdir, 'links.csv')) as f:
        reader = csv.DictReader(f)
        links = {}
        for row in reader:
            links[row['id']] = {
                'cwsac': row['cwsac_id'] if row['cwsac_id'] != '' else None,
                'dbpedia': row['dbpedia_url']
            }
    build_battles(data, links, path.join(dst, 'civilwarorg_battles.csv'))
    build_forces(data, path.join(dst, 'civilwarorg_forces.csv'))
    build_commanders(data, path.join(dst, 'civilwarorg_commanders.csv'))


def main():
    src, dst = sys.argv[1:3]
    build(src, dst)


if __name__ == '__main__':
    main()
