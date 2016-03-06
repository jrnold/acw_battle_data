####################
phisterer_to_dbpedia
####################

:name: phisterer_to_dbpedia
:path: phisterer_to_dbpedia.csv
:format: csv

Concordance between battles in ``phisterer_battles`` and dbpedia.org URIs.

See :doc:`phisterer_to_cwsac` for notes on specific battles.


Sources: [Phisterer1883]_


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


Identifier of battle in the Phisterer data (:doc:`phisterer_battles`).


       
to
--

:title: to
:type: string
:format: default


URI of the battle in dbpedia.org.


       
relation
--------

:title: relation
:type: string
:format: default
:constraints:
    :enum: ['eq', 'lt', 'gt']
    

Relationship between the events:
- "eq": same event - "gt": ``from`` includes ``to`` (``to`` is a part of ``from``). - "lt": ``from`` is included by ``to`` (``from`` is part of ``to``).


       

