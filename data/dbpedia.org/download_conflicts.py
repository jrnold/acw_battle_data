#!/usr/bin/env python3
"""
Download dbpedia resources for all conflicts in the American Civil War.
"""
from utils import query_or_load, download_ntriples

if __name__ == "__main__": 
    results_store = 'conflicts.json'
    query = """
select distinct ?s where {
  {?s dcterms:subject [skos:broader category:Battles_of_the_American_Civil_War]}
  UNION
  {?s dbpedia-owl:isPartOfMilitaryConflict dbpedia:American_Civil_War ; a dbpedia-owl:MilitaryConflict}
  FILTER (!regex(str(?s), "Never_Call_Retreat"))
}
"""
    results = query_or_load(query, results_store)
    resources = [x['s']['value'] for x in results['results']['bindings']]
    download_ntriples(resources, "battles/dbpedia", sleep = 4)
    

