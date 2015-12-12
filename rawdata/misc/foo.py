import yaml
import re
from collections import OrderedDict

with open("ships.yaml", "r") as f:
    data = yaml.load(f)

ships = {}
for k, v in data.items():
    if 'US' in v:
        newlist = []        
        for x in v['US']:
            if isinstance(x, list) and len(x) == 2:
                x = x[1]
            else:
                x = x[0]
            newlist.append(x.replace("_", " "))
            ships[(x, 'US')] = {'name': x, 'belligerent': 'US'}
        v['US'] = sorted(newlist)
    if 'Confederate' in v:
        newlist = []
        for x in v['Confederate']:
            if isinstance(x, list) and len(x) == 2:
                x = x[1]
            else:
                x = x[0]
            newlist.append(x.replace("_", " "))
            ships[(x, 'Confederate')] = {'name': x, 'belligerent': 'Confederate'}
            v['Confederate'] = sorted(newlist)

newships = []
for k, v in newships.items():
    newships.append({'name', 

newdata = {}
newdata['battles'] = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
newdata['ships'] = sorted(ships.items(), key=lambda t: t[0])

with open("foo.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style = False)

            
