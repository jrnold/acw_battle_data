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


# [1005,3] [non-castable-value] Row 1005 has non castable value 1864-10-26- in column 3 (type: date, format: default)
# [1785,3] [non-castable-value] Row 1785 has non castable value 1863-5--- in column 3 (type: date, format: default)
# [2104,3] [non-castable-value] Row 2104 has non castable value 1863-6-9.0 in column 3 (type: date, format: default)
# [2104,4] [non-castable-value] Row 2104 has non castable value 1863-6-9.0 in column 4 (type: date, format: default)
# [2125,3] [non-castable-value] Row 2125 has non castable value 1863-1---- in column 3 (type: date, format: default)
# [2369,3] [non-castable-value] Row 2369 has non castable value 1864-4-19-20 in column 3 (type: date, format: default)
# [2478,3] [non-castable-value] Row 2478 has non castable value 1863-5---- in column 3 (type: date, format: default)
# [2571,3] [non-castable-value] Row 2571 has non castable value 1863-3--- in column 3 (type: date, format: default)


def parse_date(dct):
    date = re.sub(' +', '', dct['date'])
    date = re.sub('---+', '--', date)
    if date == "11/301864":
        date = "11/30/1864"
    elif date == "5/1863":
        date = "5/--/1863"
    beginDate = dct['beginDate']
    m, d, y = date.split('/')
    if beginDate:
        beginDate = re.sub('---+', '--', beginDate)
        m0, d0, y0 = beginDate.split('/')
    else:
        m0 = m
        d0 = d
        y0 = y
    unknown_day = False
    if re.match("-+$", d):
        d = 15
        unknown_day = True
    elif len(d.split('-')) > 1:
        d0, d = d.split('-')
    if d0 == "26-":
        d0 = "26"
    elif d0 == "--":
        d0 = "15"
        unknown_day = True
    elif d0 == "9.0":
        d0 = "9"
    elif d0 == "19-20":
        d0 = "19"
        d = "20"
    if d == "9.0":
        d = "9"        
    beginDate = "%02d-%02d-%02d" % (int(y0), int(m0), int(d0))
    endDate = "%02d-%02d-%02d" % (int(y), int(m), int(d))
    dct['beginDate'] = beginDate
    dct['endDate'] = endDate
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
