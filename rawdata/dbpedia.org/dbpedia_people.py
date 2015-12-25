#!/usr/bin/env python3
import csv

from utils import query_dbpedia

CATEGORY_QUERY_TEMPLATE = """
SELECT DISTINCT ?person WHERE {
  ?person dct:subject %s ;
  a foaf:Person . 
} 
"""

def query_category(category):
    results = query_dbpedia(CATEGORY_QUERY_TEMPLATE % category)
    return [x['person']['value']
            for x in results['results']['bindings']]

def main():
    categories =  ('Union_Army_generals',
                   'Union_Army_colonels',
                   'Union_Army_officers',
                   'Union_Army_soldiers',
                   'Union_Army_personnel',
                   'Union_Navy_admirals',
                   'Union_Navy_officers',
                   'Union_Navy_sailors',
                   'Union_Navy_personnel',
                   'Confederate_States_Army_generals',
                   'Confederate_States_Army_officers',
                   'Confederate_States_Army_soldiers',
                   'Confederate_States_Army_personnel',
                   'Confederate_States_Navy_admirals',
                   'Confederate_States_Navy_officers',
                   'Confederate_States_Navy_sailors',
                   'Confederate_States_Navy_personnel')
    data = {}
    people = set()
    for cat in categories:
        data[cat] = query_category("dbc:%s" % cat)
        for person in data[cat]:
            people.add(person)
    ret = []
    for person in people:
        row = {'uri': person}
        for cat in categories:
            row[cat] = int(person in data[cat])
        ret.append(row)
    with open('people.csv', 'w') as f:
        fields = ['uri'] + list(categories)
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        writer.writerows(ret)

if __name__ == "__main__":
    main()
    
