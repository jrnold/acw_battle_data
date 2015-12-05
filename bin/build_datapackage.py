#!/usr/bin/env python3
"""
Combine individual metadata json files into datapackage.json
"""
import json
import sys
import os
from os import path
import fnmatch

def build(src, dst):
    with open(path.join(src, 'data.json'), 'r') as f:
        data = json.load(f)
    data['resources'] = []
    for filename in os.listdir(path.join(src, 'resources')):
        if fnmatch.fnmatch(filename, '*.json'):
            with open(path.join(src, 'resources', filename), 'r') as f:
                res = json.load(f)
                data['resources'].append(res)
    with open(dst, 'w') as f:
        json.dump(data, f)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build(src, dst)

if __name__ == '__main__':
    main()
