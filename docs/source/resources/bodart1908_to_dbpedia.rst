######################################################################
Correspondence between Bodart (1908) battles and dbpedia.org resources
######################################################################

:name: bodart1908_to_dbpedia
:path: bodart1908_to_dbpedia.csv
:format: csv

Correspondence between battles in Bodart (1908) and dbpedia.org URIs.

This is the correpsondence between battles in Bodart (1908), e.g. :doc:`bodart1908_battles`, and URIs of dbpedia.org resources.


Sources: [Bodart1908]_


Schema
======



========  ======  ========
from      string  from
to        string  to
relation  string  relation
========  ======  ========

from
----

:title: from
:type: string
:format: default


Identifier of the battle in ``bodart1908_battles.battle_id``


       
to
--

:title: to
:type: string
:format: default


Identifier of the battle in dbpedia.org.


       
relation
--------

:title: relation
:type: string
:format: default
:constraints:
    :enum: ['eq', 'lt', 'gt']
    

Relationship between the events:
- "eq": same event - "gt": ``from`` includes ``to`` (``to`` is a part of ``from``). - "lt": ``from`` is included by ``to`` (``from`` is part of ``to``).


       

