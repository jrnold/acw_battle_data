##################################################################
Correspondence between battles in ``fox_forces`` and CWSAC battles
##################################################################

:name: fox_forces_to_cwsac
:path: data/fox_forces_to_cwsac.csv
:format: csv

Correspondence between the observations in the revised Fox battle data (:doc:`fox_forces`) and the battle identifiers used by the National Park Servie CWSAC (e.g. :doc:`cwsac_battles`).


**Sources:**
- fox1898regimental


Schema
======

===========  ======  ===========
belligerent  string  Belligerent
battle_name  string  Battle Name
cwsac_id     string  CWSAC Id.
relation     string  Relation
===========  ======  ===========

belligerent
-----------

:title: Belligerent
:type: string
:format: default





       
battle_name
-----------

:title: Battle Name
:type: string
:format: default


Battle name in the ``fox_forces`` data.


       
cwsac_id
--------

:title: CWSAC Id.
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{3}[0-9]{2}[A-Z]?
    

CWSAC battle identification code.


       
relation
--------

:title: Relation
:type: string
:format: default
:constraints:
    :enum: ['<', '>', '=']
    




       

