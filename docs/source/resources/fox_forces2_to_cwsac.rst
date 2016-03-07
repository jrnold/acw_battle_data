################################################
Correspondence ``fox_forces2`` and CWSAC battles
################################################

:name: fox_forces2_to_cwsac
:path: fox_forces2_to_cwsac.csv
:format: csv

Correspondence between the observations in the revised Fox battle data (:doc:`fox_forces2`) and the battle identifiers used by the National Park Servie CWSAC (e.g. :doc:`cwsac_battles`).


Sources: [fox1898regimental]_


Schema
======



===========  ======  ============
belligerent  string  belligerent
battle_name  string  Battle Name
to           string  to
relation     string  Relationship
===========  ======  ============

belligerent
-----------

:title: belligerent
:type: string
:format: default
:constraints:
    :enum: ['Confederate', 'US']
    




       
battle_name
-----------

:title: Battle Name
:type: string
:format: default


Battle name in :doc:`fox_forces2`.


       
to
--

:title: to
:type: string
:format: default





       
relation
--------

:title: Relationship
:type: string
:format: default
:constraints:
    :enum: ['gt', 'lt', 'eq']
    

Relationship between the events:
- "eq": same event - "gt": ``from`` includes ``to`` (``to`` is a part of ``from``). - "lt": ``from`` is included by ``to`` (``from`` is part of ``to``).


       

