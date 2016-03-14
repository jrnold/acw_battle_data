import yaml


with open('rawdata/clodfelter2008/clodfelter.yaml', 'r') as f:
    data = yaml.load(f)

for battle in data:
    battle['battle_id'] = battle['battle']
    del battle['battle']

with open('clodfelter.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style = False)
