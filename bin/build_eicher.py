#!/usr/bin/env python
import csv
import sys
import os.path as path
import shutil

def build(src, dst):
    with open(path.join(src, "rawdata", "eicher", "chronology.csv"), 'r') as f:
        data = [row for row in csv.DictReader(f)]
    for row in data:
        if row['superevent'] is None:
            row['superevent'] = row['event']
    outfile = path.join(dst, "eicher_chronology.csv")
    print("Writing to %s" % dst)
    with open(outfile, 'w') as f:
        writer = csv.DictWriter(f, ('date', 'event', 'superevent', 'subevent'))
        writer.writeheader()
        writer.writerows(data)

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()
