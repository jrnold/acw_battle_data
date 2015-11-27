#!/usr/bin/env python3
import sys
import shutil
import os
import fnmatch
from os import path

def build(src, dst):
    for filename in os.listdir(src):
        if fnmatch.fnmatch(filename, "shenandoah_*.csv"):
            shutil.copy(path.join(src, filename), dst)

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()
