#!/usr/bin/env python3
import csv

from utils import query_dbpedia

CATEGORY_QUERY_TEMPLATE = """
SELECT DISTINCT ?ship WHERE {
  ?ship dct:subject/skos:broader* %s .
} 
"""

def query_category(category):
    results = query_dbpedia(CATEGORY_QUERY_TEMPLATE % category)
    return [x['ship']['value']
            for x in results['results']['bindings']]

def main():
    categories =  ('Ships_of_the_Union_Navy',
                   'Ships_of_the_Confederate_States_Navy')
    data = {}
    ships = set()
    for cat in categories:
        data[cat] = query_category("dbc:%s" % cat)
        for ship in data[cat]:
            ships.add(ship)
    ret = []
    for ship in ships:
        row = {'uri': ship,
               'union': int(ship in 'Ships_of_the_Union_Navy'),
               'confederate': int(ship in 'Ships_of_the_Confederate_States_Navy')}
        ret.append(row)
    with open('dbpedia_ships.csv', 'w') as f:
        fields = ('uri', 'union', 'confederate')
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        writer.writerows(ret)

if __name__ == "__main__":
    main()
    
