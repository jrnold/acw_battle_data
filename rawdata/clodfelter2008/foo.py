import csv
import yaml
from os import path

with open(path.expanduser("clodfelter.yaml"), "r") as f:
    data = yaml.load(f)

for battle in data:
    for k in battle["forces"]:
        for cdr in battle["forces"][k]['commanders']:
            cdr['navy'] = (cdr['navy'] == '1')

with open("clodfelter-new.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style = False)
