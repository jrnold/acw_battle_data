############################################################
Correspondence between Wikipedia articles and CWSAC battles.
############################################################

:name: wikipedia_to_cwsac
:path: wikipedia_to_cwsac.csv
:format: csv



Sources: 


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


URL of the battle in Wikipedia.


       
to
--

:title: to
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

Identifier of the battle in CWSAC. See :doc:`cwsac_battles`.


       
relation
--------

:title: relation
:type: string
:format: default
:constraints:
    :enum: ['eq', 'lt', 'gt']
    

Relationship between the events:
- "eq": same event - "gt": ``from`` includes ``to`` (``to`` is a part of ``from``). - "lt": ``from`` is included by ``to`` (``from`` is part of ``to``).


       

