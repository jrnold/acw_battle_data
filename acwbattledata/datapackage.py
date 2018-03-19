#!/usr/bin/env python3
"""
Combine individual metadata files into datapackage.json
"""
import fnmatch
import hashlib
import json
import logging
import os
import sys
from os import path

import yaml

LOGGER = logging.getLogger(__name__)

def get_source_dict(filename):
    with open(filename, 'r', encoding='utf8') as f:
        citations = yaml.load(f)
    for k in citations:
        citations[k]['name'] = k
    return citations


def replace_sources(keys, sources):
    newsrc = []
    for k in keys:
        if k in sources:
            newsrc.append(sources[k])
        else:
            print("ERROR: source %s not found" % k)
    return newsrc


def replace_all_sources(bib, data):
    sources = get_source_dict(bib)
    data['references'] = sources
    for res in data['resources']:
        if 'sources' in res:
            res['sources'] = replace_sources(res['sources'], sources)
        else:
            res['sources'] = []
        if 'schema' in res:
            for col in res['schema']['fields']:
                try:
                    col['sources'] = replace_sources(col['sources'], sources)
                except KeyError:
                    pass


# From http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128 * md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def process_metadata(filename):
    with open(filename, 'r', encoding='utf8') as f:
        data = yaml.load(f)
    description = path.join(filename).replace('.yaml', '.rst')
    if path.exists(description):
        with open(description, 'r', encoding='utf8') as f:
            description_text = f.read()
            data['description'] = description_text
    return data


def process_dpkg(filename):
    return process_metadata(filename)


def process_resource(filename):
    meta = process_metadata(filename)
    if meta:
        if path.exists(meta['path']):
            meta['bytes'] = path.getsize(meta['path'])
            meta['hash'] = md5sum(meta['path'])
            meta['path'] = path.basename(meta['path'])
            return meta
        else:
            LOGGER.error(f"{filename}: {meta['path']} does not exist")
    else:
        LOGGER.error(f"{filename} has no metadata.")


def build(src, dst):
    metadir = path.join(src, 'rawdata', 'metadata')
    meta_res_dir = path.join(metadir, 'resources')
    data = process_dpkg(path.join(metadir, 'datapackage.yaml'))
    data['resources'] = []
    for filename in sorted(os.listdir(meta_res_dir)):
        if fnmatch.fnmatch(filename, '*.yaml'):
            res = process_resource(path.join(meta_res_dir, filename))
            if res:
                data['resources'].append(res)
    bib = path.join(metadir, 'sources.yaml')
    replace_all_sources(bib, data)
    with open(path.join(dst, 'datapackage.json'), 'w', encoding="utf8") as f:
        json.dump(data, f, indent=2)
        print("Writing: %s" % path.join(dst, 'datapackage.json'))


def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build(src, dst)


if __name__ == '__main__':
    main()
