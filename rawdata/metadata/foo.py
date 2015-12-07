import yaml
import os
import fnmatch
from os import path

for fn in os.listdir("resources"):
    if fnmatch.fnmatch(fn, "dyer_*.yaml"):
        print(fn)
        with open(path.join("resources", fn), "r") as f:
            data = yaml.load(f)
        data['sources'] = list(set(data['sources'] + ['DyerBattles']))
        with open(path.join("resources", fn), "w") as f:
            data = yaml.dump(data, f, default_flow_style = False, allow_unicode = True)
        
