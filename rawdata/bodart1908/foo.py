import yaml


with open('bodart.yaml', 'r') as f:
    data = yaml.load(f)

for battle in data:
    if 'cwsac' in battle:
        ids = [x['uri'] for x in battle['cwsac']]
        battle['cwsac'] = {'ids': ids, 'relation': 'eq'}

with open('bodart_new.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style = False)
