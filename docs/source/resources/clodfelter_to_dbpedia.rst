#####################
clodfelter_to_dbpedia
#####################

:name: clodfelter_to_dbpedia
:path: clodfelter_to_dbpedia.csv
:format: csv



Sources: [Clodfelter2008]_


Schema
======



========  ======  ============
from      string  Belligerent
to        string  Debpedia URI
relation  string  Relationship
========  ======  ============

from
----

:title: Belligerent
:type: string
:format: default





       
to
--

:title: Debpedia URI
:type: string
:format: default


dbpedia.org URI.


       
relation
--------

:title: Relationship
:type: string
:format: default
:constraints:
    :enum: ['gt', 'lt', 'eq']
    

Relationship between the events:
- "eq": same event - "gt": ``from`` includes ``to`` (``to`` is a part of ``from``). - "lt": ``from`` is included by ``to`` (``from`` is part of ``to``).


       

