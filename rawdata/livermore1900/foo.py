import csv
import json
import yaml

with open('livermore.csv', 'r', encoding="utf8") as f:
    reader = csv.DictReader(f)
    idmap = dict((int(x['par_id']), int(x['battle_id'])) for x in reader)

with open('livermore_to_cwsac.yaml', 'r', encoding="utf8") as f:
    data = yaml.load(f)

for x in data:
    for battle in x['battles_from']:
        battle['id'] = idmap[int(battle['id'])]
    x['battles_cwsac'] = x['cwsac']
    del x['cwsac']

with open('livermore_to_cwsac_new.yaml', 'w', encoding="utf8") as f:
    yaml.dump(data, f, default_flow_style = False)
