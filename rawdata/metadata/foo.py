import yaml
import os
import fnmatch
from os import path

for fn in os.listdir("resources"):
    if fnmatch.fnmatch(fn, "*.yaml"):
        print(fn)
        with open(path.join("resources", fn), "r") as f:
            data = yaml.load(f)
        try:
            del data['description']
        except KeyError:
            pass
        with open(path.join("resources", fn), "w") as f:
            data = yaml.dump(data, f, default_flow_style = False, allow_unicode = True)
        
