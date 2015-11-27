#!/usr/bin/env python3
import os
from os import path
import shutil
import sys
import subprocess as sp

PYTHON = 'python3'
RSCRIPT = 'Rscript'

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

def build_bodart(dst):
    print("build_bodart")
    sp.run([PYTHON, "bin/build_bodart.py", "rawdata/bodart1908", dst])

def build_dyer(dst):
    print("build_dyer")
    sp.run([PYTHON, "bin/build_dyer.py", "rawdata/dyer1908", dst])

def build_wikipedia(dst):
    print("build_wikipedia")
    sp.run([PYTHON, "bin/build_wikipedia.py", "rawdata/en.wikipedia.org", dst])

def build_fox(dst):
    print("build_fox")
    sp.run([RSCRIPT, "bin/build_fox.R", "rawdata/fox1898", dst])

def build(dst_dir):
    try:
        os.mkdir(dst_dir)
    except OSError:
        pass
    build_unit_sizes(dst_dir)    
    build_aad(dst_dir)
    build_cwsac(dst_dir)
    build_cwsac2(dst_dir)
    build_cwss(dst_dir)
    build_bodart(dst_dir)
    build_dyer(dst_dir)
    build_wikipedia(dst_dir)
    build_fox(dst_dir)
    
def main():
    DST = sys.argv[1]
    build(DST)

if __name__ == "__main__":
    main()
