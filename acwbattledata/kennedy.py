"""Create csv files from bodart1908/battles.py."""
import csv
import os.path
import sys

import yaml

CATEGORIES = ("battle", "meeting", "surrender", "siege", "capture")


def dict_remove(x, exclude=[]):
    """Remove keys from a dict."""
    return dict((k, v) for k, v in x.items() if k not in exclude)


def dict_subset(x, include=[]):
    """Subset a dict."""
    return dict((k, v) for k, v in x.items() if k in include)


def forces_csv(src, dst):
    """Write Kennedy force level data to csv."""
    with open(src, 'r', encoding="utf8") as f:
        data = yaml.load(f)
    fieldnames = ('battle_id', 'belligerent', 'casualties_min',
                  'casualties_max', 'killed_wounded_min', 'killed_wounded_max',
                  'missing')
    with open(dst, 'w', encoding="utf8") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle in data:
            if battle['forces']:
                try:
                    battles_aggregated = ' '.join(battle['casualties_battles'])
                except KeyError:
                    battles_aggregated = battle['battle_id']
                for belligerent in battle['forces']:
                    row = battle['forces'][belligerent]
                    row['belligerent'] = belligerent
                    row['battle_id'] = battles_aggregated
                    writer.writerow(row)


def battles_csv(src, dst):
    """Write Kennedy battle-level data to csv."""
    with open(src, 'r', encoding="utf8") as f:
        data = yaml.load(f)
    fieldnames = ('battle_id', 'battle_name', 'state', 'county', 'start_date',
                  'end_date', 'casualties_min', 'casualties_max',
                  'casualties_text', 'cwsac_id')
    with open(dst, 'w', encoding="utf8") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle in data:
            row = battle.copy()
            if 'cwsac_id' not in row:
                row['cwsac_id'] = row['battle_id']
            row = dict_subset(row, fieldnames)
            writer.writerow(row)


def build(src, dst):
    """Create all output files for the Kennedy data."""
    filename = os.path.join(src, "rawdata", "kennedy1997", "kennedy1997.yaml")
    battles_csv(filename, os.path.join(dst, "kennedy1997_battles.csv"))
    forces_csv(filename, os.path.join(dst, "kennedy1997_forces.csv"))


def main():
    """Command-line interface."""
    src, dst = sys.argv[1:3]
    build(src, dst)


if __name__ == "__main__":
    main()
