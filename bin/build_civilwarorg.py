""" Convert cwsac.json to csv files """
import json
import csv
import sys
import shutil
import re
import datetime
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

MONTHS = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

REGEX_DATE = re.compile(''.join(('(?P<m>%s) (?P<d>\d+)',
                                '(?: - (?P<m2>%s)? *(?P<d2>\d+))?',
                                ', (?P<year>\d{4})'))
                        % ('|'.join(MONTHS), '|'.join(MONTHS)))

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
        

def build_battles(data, links, dst):
    fields = ('id',
              'name',
              'url',
              'start_date',
              'end_date',
              'alternate_names',
              'location',
              'state',
              'campaign',              
              'result',
              'total_casualties',
              'total_strength',
              'cwsac_id')
    with open(dst, 'w') as f:
        print("Writing: %s" % dst)
        writer = csv.DictWriter(f, fields, extrasaction = 'ignore')
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
                month2 = MONTHS.index(m.group('m2')) + 1 if m.group('m2') else month1
                row['start_date'] = datetime.date(year, month1, day1)
                if row['id'] == 'stones-river':
                    row['start_date'] = row['start_date'].replace(year = 1862)
                row['end_date'] = datetime.date(year, month2, day2)
            else:
                print(row['dates'])
            row['cwsac_id'] = links[row['id']]
            writer.writerow(row)

def build(src, dst):
    srcdir = path.join(src, 'rawdata', 'civilwar.org')
    srcfile = path.join(srcdir, 'civilwar.org.json')
    with open(srcfile, 'r') as f:
        data = json.load(f)
    with open(path.join(srcdir, 'cwsac_links.csv')) as f:
        reader = csv.DictReader(f)
        links = {}
        for row in reader:
            links[row['id']] = row['cwsac_id']
    build_battles(data, links, path.join(dst, 'civilwarorg_battles.csv'))
    build_forces(data, path.join(dst, 'civilwarorg_forces.csv'))
    build_commanders(data, path.join(dst, 'civilwarorg_commanders.csv'))

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == '__main__':
    main()
