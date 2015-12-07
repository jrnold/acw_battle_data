import yaml
import re

with open("clodfelter.yaml", "r") as f:
    data = yaml.load(f)

def rename(x, k, j):
    if k in x:
        x[j] = x[k]
        del x[k]
          
for battle in data:
    for belligerent in battle['forces']:
          for k in battle['forces'][belligerent]:
             if ' ' in k:
                 rename(battle['forces'][belligerent], k, re.sub(' ', '_', k))

with open("clodfelter-new.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style = False)
