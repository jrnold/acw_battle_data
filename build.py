#!/usr/bin/env python3
import os
from os import path
import shutil
import subprocess as sp
import argparse

PYTHON = 'python'
RSCRIPT = 'Rscript'

SRC = "."

def build_aad(src, dst):
    print("build_aad")
    sp.check_call([PYTHON, 'bin/build_aad.py', src, dst])

def build_cwsac(src, dst):
    print("build_cwsac")
    sp.check_call([PYTHON, 'bin/build_cwsac.py', src, dst])
    sp.check_call([RSCRIPT, 'bin/update_cwsac_forces.R', src, dst])

def build_cws2(src, dst):
    print("build_cws2")
    sp.check_call([PYTHON, 'bin/build_cws2.py', src, dst])
    sp.check_call([RSCRIPT, 'bin/update_cws2_forces.R', src, dst])    

def build_cwss(src, dst):
    print("build_cwss")
    sp.check_call([PYTHON, 'bin/build_cwss.py', src, dst])

def build_unit_sizes(src, dst):
    print("build_unit_sizes")
    shutil.copy(path.join(src, 'rawdata', 'unit_sizes', 'unit_sizes.csv'), dst)
    shutil.copy(path.join(src, 'rawdata', 'unit_sizes', 'eicher_units_table.csv'), dst)

def build_bodart(src, dst):
    print("build_bodart")
    sp.check_call([PYTHON, "bin/build_bodart.py", src, dst])

def build_dyer(src, dst):
    print("build_dyer")
    sp.check_call([PYTHON, "bin/build_dyer.py", src, dst])

def build_wikipedia(src, dst):
    print("build_wikipedia")
    sp.check_call([PYTHON, "bin/build_wikipedia.py", src, dst])

def build_fox(src, dst):
    print("build_fox")
    sp.check_call([RSCRIPT, "bin/build_fox.R", src, dst])

def build_greer(src, dst):
    print("build_greer")
    shutil.copy(path.join(src, "rawdata", "greer2005", "greer2005_weekly_casualties.csv"), dst)

def build_kennedy(src, dst):
    print("build_kennedy")
    sp.check_call([PYTHON, "bin/build_kennedy.py", src, dst])

def build_livermore(src, dst):
    print("build_livermore")
    sp.check_call([RSCRIPT, "bin/build_livermore.R", src, dst])
            

def build_thorpe(src, dst):
    print("build_thorpe")
    sp.check_call([PYTHON, "bin/build_thorpe.py", src, dst])

def build_nyt(src, dst):
    print("build_nyt")
    shutil.copy(path.join(src, "rawdata", "nytimes_civil_war_chronology",
                          "nytimes_civil_war_chronology.json"), dst)

def build_phisterer(src, dst):
    print("build_phisterer")
    sp.check_call([PYTHON, "bin/build_phisterer.py", src, dst])

def build_shenandoah(src, dst):
    print("build_shenandoah")
    sp.check_call([PYTHON, "bin/build_shenandoah.py", src, dst])

def build_clodfelter(src, dst):
    print("build_clodfelter")
    sp.check_call([PYTHON, "bin/build_clodfelter.py", src , dst])
    sp.check_call([RSCRIPT, "bin/update_clodfelter_forces.R", src, dst])

def build_nps(src, dst):
    print("build_nps")
    sp.check_call([RSCRIPT, "bin/build_nps_combined.R", src, dst])

def build_cdb90(src, dst):
    print("build_cdb90")
    sp.check_call([RSCRIPT, "bin/build_cdb90.R", src, dst])

def build_civilwarorg(src, dst):
    print("build_civilwarorg")
    sp.check_call([PYTHON, "bin/build_civilwarorg.py", src, dst])
    
def build_misc(src, dst):
    print("build_misc")
    sp.check_call([PYTHON, "bin/build_misc.py", src, dst])

def build_ships(src, dst):
    print("build_ships")
    sp.check_call([PYTHON, "bin/build_ships.py", src, dst])
    
def build_metadata(src, dst):
    print("build_metadata")
    sp.check_call([PYTHON, "bin/build_metadata.py", src, dst])

def build_datapackage(src, dst):
    print("build_datapackage")
    sp.check_call([PYTHON, "bin/build_datapackage.py", src, dst])

def build_docs(src, dst, docs, bucket):
    print("build_docs")
    # create docs sources
    sp.check_call([PYTHON, "bin/build_docs.py", src, dst, docs, bucket])

def build(src, dst, docs, bucket):
    if path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    build_unit_sizes(src, dst)    
    build_aad(src, dst)
    build_shenandoah(src, dst)    
    build_cwsac(src, dst)
    build_cws2(src, dst)
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
    build_ships(src, dst)
    build_civilwarorg(src, dst)    
    build_misc(src, dst)
    # metadata
    build_metadata(src, dst)
    build_datapackage(src, dst)
    # build docs
    build_docs(src, dst, docs, bucket)
           
def main():
    parser = argparse.ArgumentParser(description = "Build the ACW battle data")
    parser.add_argument('dst', metavar = 'DST', default = "data", nargs = '?',
                        help = "data build directory")
    parser.add_argument('--bucket', metavar = 'BUCKET',
                        default = "data.jrnold.me",
                        help = "AWS bucket with the data")
    
    args = parser.parse_args()
    src = "."
    docs = path.join(src, "docs/source")
    build(src, args.dst, docs, args.bucket)

if __name__ == "__main__":
    main()
