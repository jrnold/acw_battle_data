#!/usr/bin/env python
import sys
import os.path as path
import shutil

def build(src, dst):
    outfile = "eicher_chronology.csv"
    print("writing %s" % outfile)
    shutil.copy(path.join(src, "rawdata", "eicher", "chronology.csv"),
                path.join(dst, outfile))

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()
