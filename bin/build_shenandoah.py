#!/usr/bin/env python3
import sys
import shutil
import os
import fnmatch
from os import path

import yaml


def get_data(src):
    data = []
    for filename in os.listdir(path.join(src, "yaml")):
        if fnmatch.fnmatch(filename, "*.yaml"):
            fn = path.join(src, "yaml", filename)
            print(fn)
            with open(fn, 'r') as f:
                print(f.read())
                data.append(yaml.load(f))
    return data

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()
