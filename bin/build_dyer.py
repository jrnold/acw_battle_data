"""Script to build all Dyer (1908) related data."""
import json
import shutil
import sys
from os import path

import yaml


def build_engagements(src, dst):
    """Build Dyer engagement data."""
    pass

def _process_mapping(row):
    newdata = {
        "battles_from": [x['battle_id'] for x in row['battles_from']],
        "battles_cwsac": [x['cwsac_id'] for x in row['battles_cwsac']],
        "diff_dates": "diff_dates" in row and row["diff_dates"],
        "diff_states": "diff_states" in row and row["diff_states"]
    }
    try:
        newdata['relation'] = row['relation']
    except KeyError:
        newdata['relation'] = "eq"
    return newdata


def build_to_cwsac(src, dst):
    """Convert YAML file with CWSAC mappings to a JSON file."""
    srcfile = path.join(src, "dyer_to_cwsac.yaml")
    dstfile = path.join(dst, "dyer_to_cwsac.json")
    with open(srcfile, 'r') as fp:
        data = yaml.load(fp)
    cleaned_data = [_process_mapping(x) for x in data]
    with open(dstfile, "w") as fp:
        json.dump(cleaned_data, fp)


def build(src, dst):
    """Build all Dyer data."""
    dyer_src = path.join(src, 'rawdata', 'dyer1908')
    build_engagements(dyer_src, dst)
    build_to_cwsac(dyer_src, dst)


def main():
    """Command line interface."""
    src, dst = sys.argv[1:3]
    build(src, dst)


if __name__ == "__main__":
    main()
