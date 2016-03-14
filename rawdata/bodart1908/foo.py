import yaml


with open('bodart.yaml', 'r') as f:
    data = yaml.load(f)

for battle in data:
    print("%s (%s - %s)" % (battle['battle_name'], battle['start_date'], battle['end_date']))
