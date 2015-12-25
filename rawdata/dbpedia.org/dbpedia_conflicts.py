#!/usr/bin/env python3
"""
Download dbpedia resources for all conflicts in the American Civil War.
"""
import csv

from utils import query_dbpedia

def download():
    query = """
SELECT DISTINCT ?s WHERE {
  {?s dct:subject/skos:broader* dbc:Battles_of_the_American_Civil_War}
  UNION
  {?s dbo:isPartOfMilitaryConflict dbr:American_Civil_War ;
      a dbo:MilitaryConflict}
   FILTER (!regex(str(?s), "Never_Call_Retreat"))
}
"""
    results = query_dbpedia(query)
    resources = [x['s']['value'] for x in results['results']['bindings']]
    with open('dbpedia_conflicts.csv', 'w') as f:
        fields = ('uri', )
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for s in resources:
            writer.writerow({'uri': s})

def main():
    download()

if __name__ == "__main__": 
    main()

