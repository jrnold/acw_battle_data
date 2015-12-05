#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:42:38 2015

@author: jrnold
"""
import yaml
import pandas
import sys
from os import path
import os

type_convert = {'int64': 'integer',
        'float64': 'number',
        'object': 'string',
        'datetime64': 'datetime',
        'bool': 'boolean'}

import pandas

def make_metadata(src):
    name, ext = path.splitext(path.basename(src))
    dformat = ext[1:]
    meta = {'name': path.splitext(path.basename(src))[0],
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
    for filename in os.listdir(src):
        dstfile = path.join(dst, path.splitext(path.basename(filename))[0]) + '.yaml'
        if not path.exists(dstfile):
            with open(dstfile, 'w') as f:
                yaml.dump(make_metadata(path.join(src, filename)), f,
                          default_flow_style=False, allow_unicode=True)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build_meta(src, dst)

if __name__ == "__main__":
    main()

    
    
