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

def build_greer(dst):
    print("build_greer")
    shutil.copy("rawdata/greer2005/greer2005_weekly_casualties.csv", dst)

def build_kennedy(dst):
    print("build_kennedy")
    src = 'rawdata/kennedy1997'
    files = ("kennedy_battles.csv", "kennedy_casualties.csv",
             "kennedy_to_cwsac.csv")
    for fn in files:
        shutil.copy(path.join(src, fn), dst)

def build_livermore(dst):
    print("build_livermore")
    sp.run([RSCRIPT, "bin/build_livermore.R", "rawdata/livermore1900",
            "dependencies/PAR/data", dst])

def build_thorpe(dst):
    print("build_thorpe")
    sp.run([PYTHON, "bin/build_thorpe.py", "rawdata/thorpe", dst])

def build_nyt(dst):
    print("build_nyt")
    shutil.copy("rawdata/nytimes_civil_war_chronology/nytimes_civil_war_chronology.json", dst)

def build_phisterer(dst):
    print("build_phisterer")
    sp.run([PYTHON, "bin/build_phisterer.py", "rawdata/phisterer1883", dst])

def build_shenandoah(dst):
    print("build_shenandoah")
    sp.run([PYTHON, "bin/build_shenandoah.py", "rawdata/shenandoah", dst])

def build_clodfelter(dst):
    print("build_clodfelter")
    sp.run([PYTHON, "bin/build_clodfelter.py", "rawdata/clodfelter2008", dst])
    
def build(dst_dir):
    try:
        os.mkdir(dst_dir)
    except OSError:
        pass
    build_unit_sizes(dst_dir)    
    build_aad(dst_dir)
    build_shenandoah(dst_dir)    
    build_cwsac(dst_dir)
    build_cwsac2(dst_dir)
    build_cwss(dst_dir)
    build_bodart(dst_dir)
    build_dyer(dst_dir)
    build_wikipedia(dst_dir)
    build_fox(dst_dir)
    build_greer(dst_dir)
    build_kennedy(dst_dir)
    build_livermore(dst_dir)
    build_thorpe(dst_dir)
    build_nyt(dst_dir)
    build_phisterer(dst_dir)
    build_clodfelter(dst_dir)
    
def main():
    DST = sys.argv[1]
    build(DST)

if __name__ == "__main__":
    main()
