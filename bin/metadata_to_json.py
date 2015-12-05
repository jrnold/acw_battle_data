import json
import os
from os import path
import sys
import fnmatch

import yaml

def build(src, dst):
    try:
        os.makedirs(dst)
    except OSError:
        pass
    try:
        os.makedirs(path.join(dst, 'resources'))
    except OSError:
        pass
    for filename in os.listdir(path.join(src, 'resources')):
        if fnmatch.fnmatch(filename, '*.yaml'):
            print(filename)
            with open(path.join(src, 'resources', filename), 'r') as f:
                data = yaml.load(f)
            description = path.join(src, 'resources', filename).replace('.yaml', '.md')
            if path.exists(description):
                with open(description, 'r') as f:
                    description_text = f.read()
                data['description'] = description_text
            with open(path.join(dst, 'resources', filename).replace('.yaml', '.json'), 'w') as f:
                json.dump(data, f)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build(src, dst)

if __name__ == '__main__':
    main()

