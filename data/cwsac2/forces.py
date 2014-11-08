import json
import yaml

with open("forces.yaml", "r") as f:
    data = yaml.load(f)

allkeys = {}    
for k, v in data.items():
    for combatant in ('US', 'CS', 'I'):
        if combatant in v:
            for j in v[combatant].keys():
                allkeys[j] = None

for x in sorted([k for k in allkeys.keys()]):
    print(x)


