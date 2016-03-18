import yaml

with open('rawdata/kennedy1997/kennedy1997.yaml', 'r') as f:
  data = yaml.load(f)

for battle in data:
  battle['state'] = battle['battle_id'][:2]
