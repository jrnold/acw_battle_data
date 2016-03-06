#########################################################################
Correspondence between Livermore (1900) battles and dbpedia.org resources
#########################################################################

:name: livermore_to_dbpedia
:path: livermore_to_dbpedia.csv
:format: csv



Sources: [Livermore1900]_


Schema
======



========  =======  ========
from      integer  from
to        string   to
relation  string   relation
========  =======  ========

from
----

:title: from
:type: integer
:format: default


Battle identifier in :doc:`livermore_battles`.


       
to
--

:title: to
:type: string
:format: url


URI in dbpedia.org.


       
relation
--------

:title: relation
:type: string
:format: default
:constraints:
    :enum: ['eq', 'lt', 'gt']
    

Relationship between the events:
- "eq": same event - "gt": ``from`` includes ``to`` (``to`` is a part of ``from``). - "lt": ``from`` is included by ``to`` (``from`` is part of ``to``).


       

