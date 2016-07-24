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
SELECT DISTINCT ?person, ?battle, ?surname, ?given, ?name WHERE {
    ?battle dbo:isPartOfMilitaryConflict dbr:American_Civil_War ;
    a dbo:MilitaryConflict .
    ?battle dbo:commander ?person .
    ?person a foaf:Person .
    OPTIONAL { ?person foaf:surname ?surname }
}
    """
    results = query_dbpedia(query)
    data = []
    for x in results['results']['bindings']:
        data.append(dict((k, x[k]['value']) for k in x))
    return data


def main():
    ret = query_commanders()
    with open('dbpedia_commanders.csv', 'w') as f:
        fields = [k for k in ret[0].keys()]
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        writer.writerows(ret)

if __name__ == "__main__":
    main()
