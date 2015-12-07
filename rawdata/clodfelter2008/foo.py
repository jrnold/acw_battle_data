import csv
import yaml
from os import path

with open(path.expanduser("clodfelter.yaml"), "r") as f:
    data = yaml.load(f)

commanders = {}
with open("../../data/nps_commanders.csv", "r") as f:
    for row in csv.DictReader(f):
        if row['belligerent'] == "Native American":
            continue
        if row['cwsac_id'] not in commanders:
            commanders[row['cwsac_id']] = {'US': [],
                                         'Confederate': []}
        keys = ('PersonID', 'last_name', 'first_name',
                'middle_name', 'middle_initial', 'rank', 'navy')
        d = dict((k, row[k]) for k in keys)
        commanders[row['cwsac_id']][row['belligerent']].append(d)

for battle in data:
    cwsac = None
    if 'cwsac' in battle:
        for x in battle['cwsac']:
            if x['relation'] == "=":
                v = commanders[x['id']]
                battle['forces']['US']['commanders'] = v['US']
                battle['forces']['Confederate']['commanders'] = v['Confederate']
                continue
    else:
        print(battle['battle'])        

with open("clodfelter-new.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style = False)
