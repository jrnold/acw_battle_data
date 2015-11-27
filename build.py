#!/usr/bin/env python3
import os
from os import path
import shutil
import sys
import subprocess as sp

PYTHON = 'python3'

def build_aad(dst_dir):
    print("build_aad")
    sp.run([PYTHON, 'bin/build_aad.py', 'rawdata/aad/events.json',
            path.join(dst_dir, 'aad_battles.csv')])
    shutil.copy('rawdata/aad/events.json',
                path.join(dst_dir, 'aad_events.json'))


def build_cwsac(dst):
    print("build_cwsac")
    sp.run([PYTHON, 'bin/build_cwsac.py', 'rawdata/cwsac', dst])

def build_cwsac2(dst):
    print("build_cwsac2")
    sp.run([PYTHON, 'bin/build_cwsac2.py', 'rawdata/cwsac2', dst])

def build_cwss(dst):
    print("build_cwss")
    sp.run([PYTHON, 'bin/build_cwss.py', 'rawdata/cwss', dst])

def build_unit_sizes(dst):
    print("build_unit_sizes")
    shutil.copy('rawdata/unit_sizes/unit_sizes.csv', dst)
    shutil.copy('rawdata/unit_sizes/eicher_units_table.csv', dst)    

def build(dst_dir):
    try:
        os.mkdir(dst_dir)
    except OSError:
        pass
    build_aad(dst_dir)
    build_cwsac(dst_dir)
    build_cwsac2(dst_dir)
    build_cwss(dst_dir)
    build_unit_sizes(dst_dir)
    
def main():
    DST = sys.argv[1]
    build(DST)

if __name__ == "__main__":
    main()
