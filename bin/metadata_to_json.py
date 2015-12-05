import json
import os
from os import path
import sys
import fnmatch
import shutil

import yaml

def process_metadata(filename):
    with open(filename, 'r') as f:
        data = yaml.load(f)
    description = path.join(filename).replace('.yaml', '.md')
    if path.exists(description):
        with open(description, 'r') as f:
            description_text = f.read()
            data['description'] = description_text
    return data

def yaml_to_json(src, dst):
    data = process_metadata(src)
    with open(dst, 'w') as f:
        json.dump(data, f)

def build(src, dst):
    if path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    os.makedirs(path.join(dst, 'resources'))
    yaml_to_json(path.join(src, 'data.yaml'),
                 path.join(dst, 'data.json'))
    resdir = path.join(src, 'resources')
    for filename in os.listdir(resdir):
        if fnmatch.fnmatch(filename, '*.yaml'):
            yaml_to_json(path.join(resdir, filename),
                         path.join(dst, 'resources',
                                   filename.replace('.yaml', '.json')))

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build(src, dst)

if __name__ == '__main__':
    main()

