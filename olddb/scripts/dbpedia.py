from os import path
import os
import json
import sys
import re
import codecs
import yaml
from datetime import datetime as datetime_
import urllib

import sqlalchemy as sa
from sqlalchemy.ext import declarative
from sqlalchemy.ext.declarative import declared_attr
import rdflib
from rdflib import RDF

from acward import csv2
from acward import util
from acward import model
# from jrnold import rdfprefix as pre

## RDF Namespaces
DBP = rdflib.Namespace('http://dbpedia.org/resource/')
DBO = rdflib.Namespace('http://dbpedia.org/ontology/')
DBCAT = rdflib.Namespace('http://dbpedia.org/resource/Category:')
DCTERMS = rdflib.Namespace('http://purl.org/dc/terms/')
GEO = rdflib.Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
GEORSS = rdflib.Namespace('http://www.georss.org/georss/')

# CONSTANTS
_oACW = 'of_the_American_Civil_War'

def has_subject(graph, s, o):
    """Does resource have skos:subject

    Checks for any triples in graph, where
    ?s skos:subject ?o
    """
    return ((s, DCTERMS['subject'], o) in graph)


def list_battles(graph):
    """List of battle resources in the rdf graph"""
    _RDF_CLASS = ACWDBP['Battle']
    return graph.subjects(RDF.type, _RDF_CLASS)

def _coord(graph, uri):
    try:
        coords = graph.objects(uri, GEORSS.point).next()
        latitude, longitude = [float(x) for x in coords.split(' ')]
    except StopIteration:
        latitude, longitude = (None, None)
    return latitude, longitude

def parse_rdf(f, theaters):
    graph = rdflib.ConjunctiveGraph()
    graph.parse(f, format='xml')
    uri = util.pop(graph.subject_objects(rdflib.RDFS.label))[0]
    
    """Generate dictionary of battle data from the rdf graph"""
    datum = {'uri': urllib.unquote(unicode(uri))}

    def _get_prop(p):
        o = util.pop(graph.objects(uri, p))
        if o: 
            return unicode(o)
        else:
            return None

    def _category(category):
        return has_subject(graph, uri, DBCAT[category])
        
    datum['date'] = util.todate(_get_prop(DBO['date']), '%Y-%m-%d')
    datum['latitude'], datum['longitude'] = _coord(graph, uri)
    datum['place'] = _get_prop(DBO['place'])
    datum['result'] = _get_prop(DBO['result'])
    ## Categories
    datum['union_victory'] = _category('Union_victories_%s' % _oACW)
    datum['confederate_victory'] = _category('Confederate_victories_%s' % _oACW)
    datum['inconclusive'] = _category('Inconclusive_battles_%s' % _oACW)
    datum['naval_battle'] = _category('Naval_battles_%s' % _oACW)
    datum['siege'] = _category('Sieges_%s' % _oACW)
    datum['massacre'] = _category('Massacres_%s' % _oACW)
    ## Lookup theater
    datum['theater'] = None
    for k, v in theaters.iteritems():
        try:
            graph.subject_objects(v).next
            datum['theater'] = k
            break
        except StopIteration:
            continue
    return model.DbpBattle(**datum)

def theater_dict():
    """ Lookup dictionary for theaters """
    def battles_of(x):
        return rdflib.URIRef(re.sub("Category:", "Category:Battles_of_the_", x))
    session = model.Session()
    return dict([(thtr.theater, battles_of(thtr.dbp_category))
                     for thtr in session.query(model.Theater).all()])

def load(datadir):
    """ Load dbpedia data to the database """
    print("loading dbp_battles")
    battledir = path.join(datadir, 'dbpedia')
    theaters = theater_dict()
    session = model.Session()
    for res in os.listdir(battledir):
        session.add(parse_rdf(path.join(battledir, res), theaters))
    session.commit()


