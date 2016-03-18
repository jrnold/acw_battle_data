#!/usr/bin/env python
import shutil
from os import path
import sys
import csv

import pandas as pd
import yaml

FILES = ('burdekin_langdana_war_trend.csv',
         'reiter2009_turning_points.csv')

def copyfiles(miscdir, dst):
    for fn in FILES:
        srcfile = path.join(miscdir, fn)
        dstfile = path.join(dst, fn)
        print("Writing %s" % dstfile)
        shutil.copy(srcfile, dstfile)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    miscdir = path.join(src , 'rawdata' , 'misc')
    copyfiles(miscdir, dst)

if __name__ == '__main__':
    main()
