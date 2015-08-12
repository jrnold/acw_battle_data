#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dump the NPS CWSS from MSSQL to csv files
"""

import sqlalchemy as sa
import os
from os import path
import csv
import re

EXT = 'tsv'

def colnames(table):
    return [c.name for c in table.columns]

def clean_el(x):
    if x:
        x = re.sub("\t", "", str(x))
    else:
        x = ''
    return x

def clean(row):
    return [clean_el(x) for x in row]

def dump_table(table, filename, header = True):
    cols = colnames(table)
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, cols, delimiter = '\t')
        if header:
            writer.writerow(cols)
        for row in table.select().execute():
            writer.writerow(clean(row))
            
def dump_to_csv(metadata, directory, header = True):
    for table in metadata.sorted_tables:
        tablename = table.name
        if (tablename == "focus"):
            outfn = path.join(directory, '%s.%s' % (tablename, EXT))
            print("dumping %s to %s" % (tablename, outfn))
            dump_table(table, outfn, header = header)
     

def main():
    ENGINE = sys.argv[1]
    DST = sys.argv[2]
    engine = sa.create_engine(ENGINE, encoding = 'latin1', convert_unicode = True)
    metadata = sa.MetaData(bind = engine, reflect = True)
    os.makedirs(DST, exist_ok = True)
    dump_to_csv(metadata, DST) 

if __name__ == '__main__':
    main()
