import sys
import os
from os import path
import json
import shutil

import jinja2

def build_index(docs, env, metadata):
    template = env.get_template('index.md')
    rendered = template.render(metadata)
    with open(path.join(docs, 'index.md'), 'w') as f:
        f.write(rendered)

def build_resources(docs, env, metadata):
    data_doc_dir = path.join(docs, 'data')
    if path.exists(data_doc_dir):
        shutil.rmtree(data_doc_dir)
    os.makedirs(data_doc_dir)
    template = env.get_template('resource.md')
    for res in metadata['resources']:
        rendered = template.render(res)
        with open(path.join(data_doc_dir, res['name'] + '.md'), 'w') as f:
            f.write(rendered)

def build(src, dst, docs):
    env = jinja2.Environment(loader = jinja2.FileSystemLoader(path.join(src, 'templates')),
                             autoescape = False)
    with open(path.join(dst, 'datapackage.json'), 'r') as f:
        metadata = json.load(f)
    print(env.list_templates())
    build_index(docs, env, metadata)
    build_resources(docs, env, metadata)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    docs = sys.argv[3]
    build(src, dst, docs)

if __name__ == '__main__':
    main()
