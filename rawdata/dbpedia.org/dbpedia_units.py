#!/usr/bin/env python3
import csv

from utils import query_dbpedia

CATEGORY_QUERY_TEMPLATE = """
SELECT DISTINCT ?unit WHERE {
  ?unit dct:subject/skos:broader* %s .
}
"""

def query_category(category):
    results = query_dbpedia(CATEGORY_QUERY_TEMPLATE % category)
    return [x['unit']['value']
            for x in results['results']['bindings']]

def main():
    categories =  ('Military_units_and_formations_of_the_Confederate_States_Army',
                   'Military_units_and_formations_of_the_Union_Army')
    data = {}
    units = set()
    for cat in categories:
        data[cat] = query_category("dbc:%s" % cat)
        for unit in data[cat]:
            units.add(unit)
    ret = []
    for unit in units:
        row = {'uri': unit,
               'union': int(unit in 'Military_units_and_formations_of_the_Union_Army'),
               'confederate': int(unit in 'Military_units_and_formations_of_the_Confederate_States_Army')}
        ret.append(row)
    with open('dbpedia_units.csv', 'w') as f:
        fields = ('uri', 'union', 'confederate')
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        writer.writerows(ret)

if __name__ == "__main__":
    main()
