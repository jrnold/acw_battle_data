###############################################
Correspondence ``fox_forces`` and CWSAC battles
###############################################

:name: fox_forces_to_cwsac
:path: fox_forces_to_cwsac.csv
:format: csv

Correspondence between the observations in the revised Fox battle data (:doc:`fox_forces`) and the battle identifiers used by the National Park Servie CWSAC (e.g. :doc:`cwsac_battles`).


Sources: [fox1898regimental]_


Schema
======



===========  ======  ============
belligerent  string  belligerent
battle_name  string  Battle Name
to           string  CWSAC Id.
relation     string  Relationship
===========  ======  ============

belligerent
-----------

:title: belligerent
:type: string
:format: default





       
battle_name
-----------

:title: Battle Name
:type: string
:format: default


Battle name in :doc:`fox_forces`.


       
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


       

