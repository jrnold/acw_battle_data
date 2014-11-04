# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 20:24:18 2014

@author: jrnold
"""
import requests

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
