"""Create Fox (1898) files."""
import json
import os.path as path
import sys

import pandas as pd
import yaml


def build_forces(src, dst):
    """Build ``fox_forces`` data."""
    data = pd.read_csv(src)
    data['from_footnote'] = data['battle_id'].str.match('[UC][1-9]+[A-Z]').\
        astype(int)
    data['aggregates_battles'] = ~data['aggregates_battles'].isnull()
    data.to_csv(dst, index=False, float_format='%g')
    print("wrote %s" % dst)


def build_outcomes(src, dst):
    """Build ``fox_outcomes`` data."""
    pd.read_csv(src).to_csv(dst, index=False)
    print("wrote %s" % dst)


def build_to_cwsac(src, dst):
    """Convert Fox mappings to CWSAC from YAML to JSON."""
    with open(src, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
    newdata = []
    for row in data:
        x = {'relation': "eq"}
        x['battles_from'] = [btl['id'] for btl in row['battles_from']]
        x['battles_to'] = [btl['id'] for btl in row['battles_cwsac']]
        newdata.append(x)
    with open(dst, 'w', encoding='utf-8') as f:
        json.dump(newdata, f)
        print("wrote %s" % dst)


def main():
    """Create all Fox (1898) files."""
    src, dst = sys.argv[1:3]
    srcdir = path.join(src, 'rawdata', 'fox1898')
    build_outcomes(
        path.join(srcdir, "fox_outcomes.csv"),
        path.join(dst, "fox_outcomes.csv"))
    build_forces(
        path.join(srcdir, 'fox_forces.csv'), path.join(dst, 'fox_forces.csv'))
    build_to_cwsac(
        path.join(srcdir, 'fox_forces_to_cwsac.yaml'),
        path.join(dst, 'fox_forces_to_cwsac.json'))


if __name__ == '__main__':
    main()
