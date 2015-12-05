import yaml
import os
import fnmatch
from os import path

for fn in os.listdir("resources"):
    if fnmatch.fnmatch(fn, "*.yaml"):
        with open(path.join("resources", fn), "r") as f:
            data = yaml.load(f)
        if not 'title' in data:
            data['title'] = data['name']
        with open(path.join("resources", fn), "w") as f:
            data = yaml.dump(data, f, default_flow_style = False, allow_unicode = True)
        
