#!/usr/bin/env python3
"""
Download dbpedia resources for all conflicts in the American Civil War.


Query for all personnel

select distinct ?person ?surname ?givenName where {
  VALUES ?category { dbc:Union_Army_generals dbc:Union_Army_colonels dbc:Union_Army_officers dbc:Union_Army_soldiers dbc:Union_Army_personnel
                     dbc:Union_Navy_officers dbc:Union_Navy_sailors dbc:Union_Navy_personnel
                     dbc:Confederate_States_Army_generals dbc:Confederate_States_Army_officers dbc:Confederate_States_Army_personnel   
                     dbc:Confederate_States_Navy_officers dbc:Confederate_States_Navy_sailors dbc:Confederate_States_Navy_personnel
                    } 
  ?person dct:subject ?category ; a foaf:Person . 
  optional { ?person foaf:surname ?surname }
  optional { ?person foaf:givenName ?givenName }



} limit 1000

Loop through this and find all categories

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
