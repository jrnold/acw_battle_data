###################
clodfelter_to_cwsac
###################

:name: clodfelter_to_cwsac
:path: clodfelter_to_cwsac.csv
:format: csv



Sources: [Clodfelter2008]_


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


Identifier of the battle in :doc:`clodfelter_battles`.


       
to
--

:title: to
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

Identifier of the battle in CWSAC.


       
relation
--------

:title: relation
:type: string
:format: default
:constraints:
    :enum: ['eq', 'lt', 'gt']
    

Relationship between the events:
- "eq": same event - "gt": ``from`` includes ``to`` (``to`` is a part of ``from``). - "lt": ``from`` is included by ``to`` (``from`` is part of ``to``).


       

