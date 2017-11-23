import sys
import os.path

import pandas as pd


def build(src, dst):
    infile = os.path.join(src, "rawdata", "greer2005",
                          "greer2005_weekly_casualties.csv")
    data = pd.read_csv(infile)
    del data['cwsac_battle_name']
    data.to_csv(os.path.join(dst, "greer2005_weekly_casualties.csv"),
                index=False)


def main():
    build(*sys.argv[1:3])


if __name__ == "__main__":
    main()
