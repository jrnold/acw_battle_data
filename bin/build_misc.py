#!/usr/bin/env python
import shutil
from os import path
import sys

FILES = ('battlemisc.csv', 'burdekin_langdana_war_trend.csv',
         'navalbattles.csv', 'reiter2009_turning_points.csv')

def build(src, dst):
    miscdir = path.join(src , 'rawdata' , 'misc')
    for fn in FILES:
        shutil.copy(path.join(miscdir, fn), dst)

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build(src, dst)
    
if __name__ == '__main__':
    main()
