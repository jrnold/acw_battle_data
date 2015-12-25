# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 20:24:18 2014

@author: jrnold
"""
import json
from os import path
import time

import requests
import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON

def dbpedia_describe(resource, fmt = 'ntriples'):
    data = {'ntriples': 'ntriples',
             'n3': 'n3',
             'json': 'json',
             'xml': 'xml',
             'odata-atom': 'atom',
             'odata-json': 'jsod'}
    sparql = {
        'json-ld': 'application/ld+json',
        'csv': 'text/csv',
        'html': 'text/html'
        }
    if fmt in data:
        r = requests.get('http://dbpedia.org/data/%s.%s' % (resource, data[fmt]))
    elif fmt in sparql:
        params = {'default-graph-uri': "http://dbpedia.org",
                  'query': 'DESCRIBE <http://dbpedia.org/resource/%s>' % resource,
                  'output': sparql[fmt]}
        r = requests.get('http://dbpedia.org/sparql',
                         params = params)
    else:
        return None
    return r.text

def query_dbpedia(query):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results    

def query_or_load(query, results_store):
    if not path.exists(results_store):
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        with open(results_store, 'w') as f:
            json.dump(results, f)
    else:
        with open(results_store, 'r') as f:
            results = json.load(f)
    return results
    
def download_ntriples(resources, outdir, sleep = 2):
    print("downloading %d resources" % len(resources))
    for i, url in enumerate(resources):
        resource = path.basename(url)
        dst = '%s/%s.ntriples' % (outdir, resource)
        if not path.exists(dst):
            print("downloading %s" % resource)
            data = dbpedia_describe(resource, "ntriples")
            with open(dst, 'w') as f:
                f.write(data)
            time.sleep(sleep)

foaf = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
prov = rdflib.Namespace("http://www.w3.org/ns/prov#")

def get_wikipedia_page(src):
    g = rdflib.Graph()
    try:
        g.load(src, format = "nt")
    except rdflib.plugins.parsers.ntriples.ParseError as e:
        print(src)
        print(e)
        return None
    wikipage =  [(str(s), str(o)) for s, p, o 
        in g.triples((None, rdflib.namespace.FOAF.isPrimaryTopicOf, None))]
    if len(wikipage) == 0:
        print(src)
    else:
        return wikipage[0]
