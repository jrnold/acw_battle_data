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

def query_commanders():
    query = """
SELECT DISTINCT ?person WHERE {
    ?battle dbo:isPartOfMilitaryConflict dbr:American_Civil_War ;
    a dbo:MilitaryConflict .
    ?battle dbo:commander ?person .
    ?person a foaf:Person
} 
    """
    results = query_dbpedia(query)
    return [x['person']['value']
            for x in results['results']['bindings']]
    

def main():
    categories =  ('Union_Army_generals',
                   'Union_Navy_admirals',
                   'Confederate_States_Army_generals',
                   'Confederate_States_Navy_admirals')
    data = {}
    people = set()
    for cat in categories:
        data[cat] = query_category("dbc:%s" % cat)
        for person in data[cat]:
            people.add(person)
    data['commanders'] = query_commanders()
    for person in data['commanders']:
        people.add(person)
    ret = []
    for person in people:
        row = {'uri': person}
        for cat in categories:
            row[cat] = int(person in data[cat])
        ret.append(row)
    with open('dbpedia_commanders.csv', 'w') as f:
        fields = ['uri'] + list(categories)
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        writer.writerows(ret)

if __name__ == "__main__":
    main()
    
