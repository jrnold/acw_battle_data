import yaml

with open('sources.yaml', 'r') as f:
    data = yaml.load(f)
for k in data:
    del data[k]['name']
with open('sources.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style = False)
