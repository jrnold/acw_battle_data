#!/usr/bin/env python3
"""
Combine individual metadata files into datapackage.json
"""
import json
import sys
import os
from os import path
import fnmatch
import hashlib

import yaml

# From http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128 * md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()

def process_metadata(filename):
    print(filename)
    with open(filename, 'r') as f:
        data = yaml.load(f)
    description = path.join(filename).replace('.yaml', '.md')
    if path.exists(description):
        with open(description, 'r') as f:
            description_text = f.read()
            data['description'] = description_text
    return data

def process_dpkg(filename):
    return process_metadata(filename)

def process_resource(filename):
    meta = process_metadata(filename)
    if meta and path.exists(meta['path']):
        meta['bytes'] = path.getsize(meta['path'])
        meta['hash'] = md5sum(meta['path'])
    else:
        print("WARNING: something wrong with %s" % filename)
    return meta

def build(src, dst):
    metadir = path.join(src, 'rawdata', 'metadata')
    data = process_dpkg(path.join(metadir, 'datapackage.yaml'))
    data['resources'] = []
    for filename in os.listdir(path.join(metadir, 'resources')):
        if fnmatch.fnmatch(filename, '*.yaml'):
            res = process_resource(path.join(metadir, 'resources', filename))
            data['resources'].append(res)
    with open(path.join(dst, 'datapackage.json'), 'w') as f:
        json.dump(data, f)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build(src, dst)

if __name__ == '__main__':
    main()
