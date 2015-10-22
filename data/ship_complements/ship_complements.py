"""
Download civil war ships and their complements from dbpedia
"""
from os import path
import json

from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
select distinct ?ship, ?complement where {
{
{?ship dcterms:subject category:Ships_of_the_Union_Navy}
UNION
{?ship dcterms:subject [skos:broader category:Ships_of_the_Confederate_States_Navy]}
}
?ship dbpprop:shipComplement ?complement
FILTER (datatype(?complement) = xsd:integer)
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

data = []
for x in results['results']['bindings']:
    data.append({'ship': x['ship']['value'],
                 'complement': x['complement']['value']})
    
with open("ships.csv", "w") as f:
    writer = csv.DictWriter(f, ('ship', 'complement'))
    writer.writeheader()
    writer.writerows(data)

