import csv
import yaml
import os.path as path

with open('fox_forces2.csv', 'r') as f:
    data = [row for row in csv.DictReader(f)]

def clean_cwsac(x):
    if x['start_date'] != x['end_date']:
        date = '%s to %s' % (x['start_date'], x['end_date'])
    else:
        date = x['start_date']
    description = '%s, %s (%s)' % (x['battle_name'], x['state'], date)
    return (x['cwsac_id'], {'id': x['cwsac_id'], 'description': description})

with open('../../data/nps_battles.csv', 'r') as f:
    cwsac = dict(clean_cwsac(x) for x in csv.DictReader(f))

ret = []
for row in data:
    if row['start_date'] == row['end_date']:
        date_range = row['start_date']
    else:
        date_range = row['start_date'] + ' to ' + row['end_date']
    description = '%s (%s)' % (row['battle_name'], date_range)
    battles_from = [{'id': row['battle_id'], 'description': description }]
    cwsac_id = row['cwsac_id'].split()
    if len(cwsac_id):
        battles_cwsac = [cwsac[id] for id in cwsac_id]
        ret.append({'battles_from': battles_from, 'battles_cwsac': battles_cwsac, 'relation' : 'eq'})

with open('fox_forces2_to_cwsac.yaml', 'w') as f:
    yaml.dump(ret, f, default_flow_style = False, Dumper = yaml.SafeDumper)
