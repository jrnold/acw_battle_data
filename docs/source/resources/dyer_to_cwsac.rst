############################################################
Correspondence between Dyer (1908) battles and CWSAC battles
############################################################

:name: dyer_to_cwsac
:path: dyer_to_cwsac.csv
:format: csv



Sources: [DyerBattles]_, [dyer1908_war_rebel]_


Schema
======



========  ======  ============
from      string  Belligerent
to        string  CWSAC Id.
relation  string  Relationship
========  ======  ============

from
----

:title: Belligerent
:type: string
:format: default





       
to
--

:title: CWSAC Id.
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{3}[0-9]{2}[A-Z]?
    

CWSAC battle identification code. See :doc:`cwsac_battles`.


       
relation
--------

:title: Relationship
:type: string
:format: default
:constraints:
    :enum: ['gt', 'lt', 'eq']
    

Relationship between the events:
- "eq": same event - "gt": ``from`` includes ``to`` (``to`` is a part of ``from``). - "lt": ``from`` is included by ``to`` (``from`` is part of ``to``).


       

