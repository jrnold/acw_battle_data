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

type_convert = {'int64': 'integer',
        'float64': 'number',
        'object': 'string',
        'datetime64': 'datetime',
        'bool': 'boolean'}

import pandas

def make_metadata(src):
    data = pandas.read_csv(src)
    name, ext = path.splitext(path.basename(src))
    dformat = ext
    schema = {'name': path.splitext(path.basename(src))[0],
              'path': src,
              'format': dformat,
              'description': ""
    }
    if dformat == "csv": 
        schema[fields] = [{'name': x,
                           'title': x,
                           'type': type_convert[data[x].dtype.name],
                           'format': 'default'}
                          for x in list(data.columns.values)]
    return schema
    
INFILE = sys.argv[1]
OUTFILE = sys.argv[2]

metadata = make_metadata(INFILE)
with open(OUTFILE, 'w') as f:
    yaml.dump(metadata, f, default_flow_style=False, allow_unicode=True)

    
    
