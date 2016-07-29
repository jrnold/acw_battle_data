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

IGNORE_FILES = ("datapackage.json", "wikipedia")

def make_metadata(src, yamlfile):
    if path.exists(yamlfile):
        with open(yamlfile, 'r') as f:
            meta = yaml.load(f)
        newfile = False
    else:
        name, ext = path.splitext(path.basename(src))
        dformat = ext[1:]
        meta = {'name': name,
                'title': name,
                'path': src,
                'format': dformat,
        }
        if dformat == 'csv':
            meta['schema'] = {'fields': []}
        newfile = True
        print("WARNING: Missing metadata file for %s" % src)

    if meta['format'] == "csv":
        fields = dict((x['name'], x) for x in meta['schema']['fields'])
        print(src)
        data = pandas.read_csv(src)
        # Remake fields
        # - fixes changes in field order
        # - adds new fields
        # TODO: warnings about deleted fields
        # TODO: check keys
        new_fields = []
        for k in fields:
            if k not in list(data.columns.values):
                print("WARNING: %s: column %s in metadata is not in data" % (src, k))
        for k in list(data.columns.values):
            try:
                new_fields.append(fields[k])
            except KeyError:
                if not newfile:
                    print("WARNING: %s: column %s not found in metadata" % (src, k))
                d = {'name': k,
                     'title': k,
                     'type': type_convert[data[k].dtype.name],
                     'format': 'default'}
                new_fields.append(d)
        meta['schema']['fields'] = new_fields
    return meta

def build_meta(src, dst):
    print("Building metadata")
    metadir = path.join(src, "rawdata", "metadata", "resources")
    for filename in os.listdir(dst):
        if not filename in IGNORE_FILES:
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
