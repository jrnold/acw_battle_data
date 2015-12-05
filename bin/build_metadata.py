#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create metadata files in yaml
"""
import pandas
import sys
from os import path
import os

import pandas
import yaml

type_convert = {'int64': 'integer',
        'float64': 'number',
        'object': 'string',
        'datetime64': 'datetime',
        'bool': 'boolean'}


def make_metadata(src, yamlfile):
    if path.exists(yamlfile):
        with open(yamlfile, 'r') as f:
            meta = yaml.load(f)
    else:
        name, ext = path.splitext(path.basename(src))
        dformat = ext[1:]
        meta = {'name': name,
                'title': name,
                'path': src,
                'format': dformat,
                'description': ""
        }
        if dformat == "csv":
            meta['schema'] = {}
            data = pandas.read_csv(src)
            meta['schema']['fields'] = [{'name': x,
                                         'title': x,
                                         'type': type_convert[data[x].dtype.name],
                                         'format': 'default'}
                                        for x in list(data.columns.values)]
    return meta


def build_meta(src, dst):
    metadir = path.join(src, "rawdata", "metadata", "resources")
    for filename in os.listdir(dst):
        if not filename in ("datapackage.json", ):
            name = path.splitext(filename)[0]
            ymlfile = path.join(metadir, name + '.yaml')
            resfile = path.join(dst, filename)
            meta = make_metadata(resfile, ymlfile)
            with open(ymlfile, 'w') as f:
                yaml.dump(meta, f, default_flow_style=False, allow_unicode=True)
                         

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build_meta(src, dst)

if __name__ == "__main__":
    main()

    
    
