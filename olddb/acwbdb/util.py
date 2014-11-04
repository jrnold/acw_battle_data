# -*- coding: utf-8 -*-
import re
import urllib
import datetime
from datetime import datetime as datetime_
import calendar

import pyparsing as pp
import rdflib

import acwbdb.rdfprefix as pre

def pop(x):
    """First object in an iterator or None

    Tries the next() method on an iterator.
    If StopIteration exception is raised, then this returns None.
    """
    try:
        ret = x.next()
    except StopIteration:
        ret = None
    return ret


def todate(x, format):
    """Convert string to date

    Catches exceptions and returns None instead.
    """
    try:
        y = datetime_.strptime(x, format).date()
    except (TypeError, ValueError):
        y = None
    return y

def insert(cls, data):
    result = cls.__table__.insert().execute(data)
    print("%d rows added to table %s" %(result.rowcount,
                                        cls.__tablename__))

def load_data(cls, file, parsef):
    insert(cls, parsef(file))

def tsv(f):
    def _split(x):
        return re.sub('(\n)?(\r)?$', '', x).split('\t')
    
    fields = _split(f.next())
    
    def _to_dict(x):
        return dict(zip(fields, _split(x)))
    
    return [_to_dict(x) for x in f]

def cast(x, f):
    try:
        y = f(x)
    except (ValueError, TypeError):
        y = None
    return y

def toint(x):
    return cast(x, int)

def interlink(triple):
    s, p, o = triple
    datum = {'urifrom': urllib.unquote(s), 'urito': urllib.unquote(o)}
    if p == pre.OWL['sameAs']:
        datum['edge'] = u'sameas'
    elif p == pre.EVENT['sub_event']:
        datum['edge'] = u'sub'
    elif p == pre.EVENT['hasSubEvent']:
        datum['edge'] = u'super'
    else:
        print("%s is not a valid relationship" % p)
    return datum

def load_interlinks(cls, source):
    graph = newgraph(source, format='n3')
    insert(cls, [interlink(spo) for spo in graph])

def newgraph(source, **kwargs):
    """Create new rdflib.ConjunctiveGraph by parsing source"""
    graph = rdflib.ConjunctiveGraph()
    graph.parse(source, **kwargs)
    return graph

def parse_date_range(x, hyphen=u"- — –", comma=u","):
    """Parse Date Ranges

    Parse date ranges like

    January 1-5, 1900
    January 1-March 1, 1900
    January 1 1900 - March 5, 1900

    """
    months = {'April': 4,
              'August': 8,
              'December': 12,
              'February': 2,
              'January': 1,
              'July': 7,
              'June': 6,
              'March': 3,
              'May': 5,
              'November': 11,
              'October': 10,
              'September': 9}
    comma = pp.oneOf(comma).suppress()
    hyphen = pp.oneOf(hyphen).suppress()
    month = pp.oneOf([k for k in months.keys()])
    month = month.setResultsName('m')
    month.addParseAction(lambda s,l,t: [months[t[0]]])
    day = pp.Word(pp.nums).setResultsName('d')
    day.addParseAction(lambda s,l,t: [int(t[0])])
    year = pp.Word(pp.nums).setResultsName('year')
    year.addParseAction(lambda s,l,t: [int(t[0])])

    start_date = (month + day + pp.Optional(comma + year)).setResultsName('start')
    start_date = (month + day + pp.Optional(comma + year)).setResultsName('start')
    end_date = (pp.Optional(month) + day + comma + year).setResultsName('end')
    date_range = start_date + pp.Optional(hyphen + end_date)
    # date_range needs to be first or one_date will pick up
    # start_dates with a year
    grammar =  date_range
    toks = grammar.parseString(x).asDict()
    d0 = toks['start']
    d1 = toks['end'] if 'end' in toks else d0
    if 'year' not in d0:
        d0['year'] = d1['year']
    if 'm' not in d1:
        d1['m'] = d0['m']
    d0date = datetime.date(*(d0[x] for x in ('year', 'm', 'd')))
    d1date = datetime.date(*(d1[x] for x in ('year', 'm', 'd')))
    return (d0date, d1date)


def parse_human_integer(x, sep=','):
    integer = pp.Word(pp.nums, min=1, max=3)
    integer3 = pp.Word(pp.nums, exact = 3)
    comma = pp.Literal(sep).suppress()
    human_int = pp.Combine(integer + pp.ZeroOrMore(comma + integer))
    human_int.setParseAction(lambda s, l, t: int(t[0]))
    return human_int.parseString(x)[0]

def parse_human_float(x, comma=',', decimal='.'):
    integer = pp.Word(pp.nums, min=1, max=3)
    integer3 = pp.Word(pp.nums, exact = 3)
    COMMA = pp.Literal(comma).suppress()
    DECIMAL = pp.Literal(decimal).suppress()
    int_part = pp.Combine(integer + pp.ZeroOrMore(COMMA + integer3))
    decimal_part = DECIMAL + pp.Word(pp.nums, min=1)
    number = int_part + pp.Optional(decimal_part)
    number.setParseAction(lambda s, l, t: float(t[0]))
    return number.parseString(x)[0]
