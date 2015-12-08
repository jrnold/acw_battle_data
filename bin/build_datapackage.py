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
import subprocess as sp

import yaml

#CITEPROC_JAVA = "citeproc-java-0.6/bin/citeproc-java"


def citeproc(bib, keys = [],
                  style = "american-political-science-association",
                  format = "text",
                  locale = "en-US",
                  citation = False,
                  ret_list = False):
    args = ["-b", bib,
            "-s", style,
            "-f", format,
            "-l", locale] + keys
    if citation:
        args.append("-c")
    if ret_list:
        args.append("--list")
    binpath = path.join("dependencies", "citeproc-java-0.6",
                        "bin", "citeproc-java")
    return sp.check_output([binpath] + args)
    
def get_keys_urls(bib):
    with open(bib, 'r', encoding = 'utf8') as f:
        data = json.load(f)
    ret = {}
    for x in data:
        try:
            ret[x['id']] = {'url': x['URL']}
        except KeyError:
            ret[x['id']] = {'url': None}
    return ret

def get_source_dict(bib):
    citations = get_keys_urls(bib)
    for k, v in citations.items():
        v['name'] = str(citeproc(bib, [k]).strip(), encoding = 'utf8')
        print(v['name'])
    citations['self'] = {'name': 'jrnold', 'email': 'jeffrey.arnold@gmail.com'}
    print(citations)
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
    try:
        data['sources'] = replace_sources(data['sources'], sources)
    except KeyError:
        pass
    for res in data['resources']:
        try:
            res['sources'] = replace_sources(res['sources'], sources)
        except KeyError:
            pass
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
    with open(filename, 'r') as f:
        data = yaml.load(f)
    description = path.join(filename).replace('.yaml', '.rst')
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
    bib = path.join(src, 'bib.json')
    replace_all_sources(bib, data)
    with open(path.join(dst, 'datapackage.json'), 'w') as f:
        json.dump(data, f)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build(src, dst)

if __name__ == '__main__':
    main()
