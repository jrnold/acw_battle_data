"""
Download dbpedia resources for all commanders in the American Civil War.
"""
#!/usr/bin/env python3
"""
Download dbpedia resources for all conflicts in the American Civil War.
"""
from utils import query_or_load, download_ntriples

if __name__ == "__main__": 
    results_store = 'commanders.json'
    query = """
select distinct ?commander where {
{
    ?battle dbpedia-owl:isPartOfMilitaryConflict dbpedia:American_Civil_War ; a dbpedia-owl:MilitaryConflict .
    ?battle dbpedia-owl:commander ?commander .
    ?commander a foaf:Person
} union {
    ?commander a yago:UnionArmyGenerals
} union {
    ?commander a yago:UnionNavyAdmirals
} union {
   ?commander a yago:ConfederateStatesArmyGenerals
} union {
   ?commander a yago:ConfederateStatesNavyAdmirals
}
}
"""
    results = query_or_load(query, results_store)
    resources = [x['commander']['value'] for x in results['results']['bindings']]
    download_ntriples(resources, "commanders", sleep=4)
