"""
Convert cwFourYearsSec.xml to a csv file
"""

import xml.etree.ElementTree as ET
import datetime
import re
import csv

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
    print(dct['date'])
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
        
    dct['beginDate'] = "%s-%s-%s" % (m0, d0, y0)
    dct['endDate'] = "%s-%s-%s" % (m, d, y)
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
            
    
def main():
    src = "cwFourYearsSec.xml"
    dst = "cwFourYearsSec.csv"
    data = parse_xml(src)
    fields = ['battleNum',
              'battleDetail',
              'beginDate',
              'endDate',
              'unknownDay',
              'lat',
              'lng',
              'shrtNm',
              'desc',
              'type',
              'killed',
              'usCasTot',
              'csCasTot']
    with open(dst, 'w') as f:
        reader = csv.DictWriter(f, fieldnames = fields)
        reader.writeheader()
        for i, row in enumerate(data):
            row['battleNum'] = i
            parse_date(row)
            reader.writerow(row)
        
if __name__ == "__main__":
    main()
    
