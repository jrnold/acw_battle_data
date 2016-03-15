import sys
import os.path as path
import json

import pandas as pd
import yaml

def build_csv(src, dst):
    pd.read_csv(src).to_csv(dst, index = False)
    print("wrote %s" % dst)

def build_to_cwsac(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    for x in data:
        x['battles_from'] = [btl['id'] for btl in x['battles_from']]
        x['battles_cwsac'] = [btl['id'] for btl in x['battles_cwsac']]
    with open(dst, 'w') as f:
        json.dump(data, f)
        print("wrote %s" % dst)

def main():
    src, dst = sys.argv[1:3]
    srcdir = path.join(src, 'rawdata', 'fox1898')
    build_csv(path.join(srcdir, "fox_outcomes.csv"),
              path.join(dst, "fox_outcomes.csv"))
    build_csv(path.join(srcdir, 'fox_forces.csv'),
                 path.join(dst, 'fox_forces.csv'))
    build_csv(path.join(srcdir, 'fox_forces2.csv'),
                  path.join(dst, 'fox_forces2.csv'))
    build_to_cwsac(path.join(srcdir, 'fox_forces_to_cwsac.yaml'),
                    path.join(dst, 'fox_forces_to_cwsac.json'))
    build_to_cwsac(path.join(srcdir, 'fox_forces2_to_cwsac.yaml'),
                    path.join(dst, 'fox_forces2_to_cwsac.json'))

if __name__ == '__main__':
    main()
