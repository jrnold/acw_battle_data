""" Data from Dyer's Compendium """
import sys
from os import path
import shutil

import yaml
import json

import requests

def build_engagements(src, dst):
    shutil.copy(path.join(src, 'engagements.csv'),
                path.join(dst, 'dyer_engagements.csv'))

def dyer_to_cwsac(src, dst):
    with open(src, 'r', encoding='utf8') as f:
        data = yaml.load(f)
    ret = []
    for battle in data:
    	if 'battles_from' in battle:
        # This is what needs work. I can't figure out how the syntax to reference the correct keys.
            battle_id = [x['battle_id'] for x in battle['battles_from']]
            cwsac_id = [x['cwsac_id'] for x in battle['battles_cwsac']]
            ret.append({'battles_from': battle_id,
                        'battles_to': cwsac_id})
    with open(dst, 'w', encoding='utf8') as f:
        json.dump(ret, f)
    print("Writing: %s" % dst)

def build(src, dst):
    dyer_src = path.join(src, 'rawdata', 'dyer1908')
    srcdir = path.join(src, "rawdata", "dyer1908")
    filename = path.join(srcdir, "dyer_to_cwsac.yaml")
    build_engagements(dyer_src, dst)
    dyer_to_cwsac(filename, path.join(dst, "dyer_to_cwsac.json"))

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()
