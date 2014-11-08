# convert yaml to csv
import json
import yaml
import csv

with open("forces.yaml", "r") as f:
    data = yaml.load(f)

allkeys = {}    
for k, v in data.items():
    for j in v.keys():
        allkeys[j] = None

for x in sorted([k for k in allkeys.keys()]):
    print(x)

