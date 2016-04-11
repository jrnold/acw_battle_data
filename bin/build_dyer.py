""" Data from Dyer's Compendium """
import sys
from os import path
import shutil

import requests

def build_engagements(src, dst):
    shutil.copy(path.join(src, 'engagements.csv'),
                path.join(dst, 'dyer_engagements.csv'))

def build(src, dst):
    dyer_src = path.join(src, 'rawdata', 'dyer1908')
    build_engagements(dyer_src, dst)

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()
