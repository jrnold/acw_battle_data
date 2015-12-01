import os
from os import path
import fnmatch
import json

SRC = "json"

for filename in os.listdir(SRC):
    if fnmatch.fnmatch(filename, "*.json"):
        with open(path.join(SRC, filename), 'r') as f:
            data = json.load(f)
        if 'I' in data['forces']:
            del data['forces']['I']
        with open(path.join(SRC, filename), 'w') as f:
            data = json.dump(data, f, indent = 2)
        
            
