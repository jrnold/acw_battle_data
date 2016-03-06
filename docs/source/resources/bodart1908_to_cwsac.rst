#################################################################
Correspondence between Bodart (1908) battles and CWSAC battle IDs
#################################################################

:name: bodart1908_to_cwsac
:path: bodart1908_to_cwsac.csv
:format: csv

Correspondence between battles in Bodart (1908) and CWSAC battle identifiers.

This is the correpsondence between battles in Bodart (1908), e.g. :doc:`bodart1908_battles`, and the battle identifiers used by the National Park Service for CWSAC battles, e.g. :doc:`cwsac_battles`.


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


Identifier of the battle in :doc:`bodart1908_battles`.


       
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


       

