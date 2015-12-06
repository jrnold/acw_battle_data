#!/usr/bin/env python3
import os
from os import path
import shutil
import sys
import subprocess as sp

PYTHON = 'python3'
RSCRIPT = 'Rscript'

SRC = "."

def build_aad(src, dst):
    print("build_aad")
    sp.run([PYTHON, 'bin/build_aad.py', src, dst])

def build_cwsac(src, dst):
    print("build_cwsac")
    sp.run([PYTHON, 'bin/build_cwsac.py', path.join(src, "rawdata", "cwsac"), dst])
    sp.run([RSCRIPT, 'bin/update_cwsac_forces.R', src, dst])

def build_cwsac2(src, dst):
    print("build_cwsac2")
    sp.run([PYTHON, 'bin/build_cwsac2.py',
            path.join(src, "rawdata", "cwsac2"), dst])
    sp.run([RSCRIPT, 'bin/update_cwsac2_forces.R', src, dst])    

def build_cwss(src, dst):
    print("build_cwss")
    sp.run([PYTHON, 'bin/build_cwss.py',
            path.join(src, "rawdata", "cwss"), dst])

def build_unit_sizes(src, dst):
    print("build_unit_sizes")
    shutil.copy(path.join(src, 'rawdata', 'unit_sizes', 'unit_sizes.csv'), dst)
    shutil.copy(path.join(src, 'rawdata', 'unit_sizes', 'eicher_units_table.csv'), dst)

def build_bodart(src, dst):
    print("build_bodart")
    sp.run([PYTHON, "bin/build_bodart.py",
            path.join(src, "rawdata", "bodart1908"), dst])

def build_dyer(src, dst):
    print("build_dyer")
    sp.run([PYTHON, "bin/build_dyer.py", src, dst])

def build_wikipedia(src, dst):
    print("build_wikipedia")
    sp.run([PYTHON, "bin/build_wikipedia.py",
            path.join(src, "rawdata", "en.wikipedia.org"), dst])

def build_fox(src, dst):
    print("build_fox")
    sp.run([RSCRIPT, "bin/build_fox.R",
            path.join(src, "rawdata", "fox1898"), dst])

def build_greer(src, dst):
    print("build_greer")
    shutil.copy(path.join(src, "rawdata", "greer2005", "greer2005_weekly_casualties.csv"), dst)

def build_kennedy(src, dst):
    print("build_kennedy")
    sp.run([PYTHON, "bin/build_kennedy.py", src, dst])

def build_livermore(src, dst):
    print("build_livermore")
    sp.run([RSCRIPT, "bin/build_livermore.R",
            src, dst])

def build_thorpe(src, dst):
    print("build_thorpe")
    sp.run([PYTHON, "bin/build_thorpe.py",
            path.join(src, "rawdata", "thorpe"), dst])

def build_nyt(src, dst):
    print("build_nyt")
    shutil.copy(path.join(src, "rawdata", "nytimes_civil_war_chronology",
                          "nytimes_civil_war_chronology.json"), dst)

def build_phisterer(src, dst):
    print("build_phisterer")
    sp.run([PYTHON, "bin/build_phisterer.py", src, dst])

def build_shenandoah(src, dst):
    print("build_shenandoah")
    sp.run([PYTHON, "bin/build_shenandoah.py",
            path.join(src, "rawdata", "shenandoah"), dst])

def build_clodfelter(src, dst):
    print("build_clodfelter")
    sp.run([PYTHON, "bin/build_clodfelter.py", src , dst])
    sp.run([RSCRIPT, "bin/update_clodfelter_forces.R", src, dst])

def build_nps(src, dst):
    print("build_nps")
    sp.run([RSCRIPT, "bin/build_nps_combined.R", src, dst])

def build_cdb90(src, dst):
    print("build_cdb90")
    sp.run([RSCRIPT, "bin/build_cdb90.R", src, dst])

def build_metadata(src, dst):
    print("build_metadata")
    sp.run([PYTHON, "bin/build_metadata.py", src, dst])

def build_datapackage(src, dst):
    print("build_datapackage")
    sp.run([PYTHON, "bin/build_datapackage.py", src, dst])

def build_docs(src, dst, docs):
    print("build_docs")
    # create docs sources
    sp.run([PYTHON, "bin/build_docs.py",
            src, dst, docs])
    sp.run(['make', '-C', 'docs', 'html'])
    sp.run(['make', '-C', 'docs', 'latexpdf'])    
    
def build(src, dst, docs):
    if path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    build_unit_sizes(src, dst)    
    build_aad(src, dst)
    build_shenandoah(src, dst)    
    build_cwsac(src, dst)
    build_cwsac2(src, dst)
    build_cwss(src, dst)
    build_nps(src, dst)
    build_bodart(src, dst)
    build_dyer(src, dst)
    build_wikipedia(src, dst)
    build_fox(src, dst)
    build_greer(src, dst)
    build_kennedy(src, dst)
    build_livermore(src, dst)
    build_thorpe(src, dst)
    build_nyt(src, dst)
    build_phisterer(src, dst)
    build_clodfelter(src, dst)
    build_cdb90(src, dst)
    # metadata
    build_metadata(src, dst)
    build_datapackage(src, dst)
    # build docs
    build_docs(src, dst, docs)
           
def main():
    src = "."
    dst = sys.argv[1]
    docs = sys.argv[2]
    build(src, dst, docs)

if __name__ == "__main__":
    main()
