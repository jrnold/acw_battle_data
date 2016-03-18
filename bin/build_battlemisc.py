import sys
import os.path as path

import pandas as pd

def build(src, dst):
    data = pd.read_csv(src)
    for i in ('siege', 'naval'):
        data[i] = data[i].fillna(0)
    data.to_csv(dst, index = False)

def main():
    src, dst = sys.argv[1:3]
    build(path.join(src, 'rawdata', 'battlemisc', 'battlemisc.csv'),
          path.join(dst, 'battlemisc.csv'))

if __name__ == '__main__':
    main()
