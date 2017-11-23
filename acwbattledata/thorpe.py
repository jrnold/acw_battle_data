#!/usr/bin/env python3
"""Convert cwFourYearsSec.xml to a csv file."""

import csv
import re
import sys
import xml.etree.ElementTree as ET
from os import path


def clean_text(tag, x):
    if x == 'null':
        x = None
    return x


def parse_date(dct):
    date = dct['date']
    if date == "11/301864":
        date = "11/30/1864"
    elif date == "5/1863":
        date = "5/--/1863"
    beginDate = dct['beginDate']
    m, d, y = date.split('/')
    if beginDate:
        m0, d0, y0 = beginDate.split('/')
    else:
        m0 = m
        d0 = d
        y0 = y
    unknown_day = False
    if d == "--" or d == "---":
        d = 15
        unknown_day = True
    elif len(d.split('-')) > 1:
        d0, d = d.split('-')

    dct['beginDate'] = re.sub(' +', '', "%s-%s-%s" % (y0, m0, d0))
    dct['endDate'] = re.sub(' +', '', "%s-%s-%s" % (y, m, d))
    dct['unknownDay'] = unknown_day
    del dct['date']


def parse_xml(src):
    tree = ET.parse(src)
    data = []
    for child in tree.getroot():
        if child.tag == "battleDetail":
            battle = {}
            battle['battleDetail'] = clean_text(child.tag, child.text)
        elif child.tag == 'copyright':
            data.append(battle)
        else:
            battle[child.tag] = clean_text(child.tag, child.text)
    return data


def build(src, dst):
    srcdir = path.join(src, "rawdata", "thorpe")
    srcfile = path.join(srcdir, "cwFourYearsSec.xml")
    dstfile = path.join(dst, "thorpe_engagements.csv")
    data = parse_xml(srcfile)
    fields = [
        'battleNum', 'battleDetail', 'beginDate', 'endDate', 'unknownDay',
        'lat', 'lng', 'shrtNm', 'desc', 'type', 'killed', 'usCasTot',
        'csCasTot'
    ]
    with open(dstfile, 'w', encoding='utf8') as f:
        reader = csv.DictWriter(f, fieldnames=fields)
        reader.writeheader()
        for i, row in enumerate(data):
            row['battleNum'] = i
            parse_date(row)
            reader.writerow(row)


def main():
    src, dst = sys.argv[1:3]
    build(src, dst)


if __name__ == "__main__":
    main()
