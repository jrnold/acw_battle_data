#########################
CWSS units in each battle
#########################

:name: CWSS battle data: units engaged
:path: data/cwss_battle_units.csv
:format: csv

Units engaged in each battle in :doc:`cwss_battles` on each side. These units correspond to units in :doc:`cwss_regiments_units`, and are largely at the size of the regiment. This data does not include naval forces.

This data was extracted from the CWSS database file ``battleunitlinks.xml``.


Sources: [CWSS]_


Schema
======



===============  ======  ================
BattlefieldCode  string  Battlefield code
Comment          string  Comment
Source           string  Source
UnitCode         string  Unit code
===============  ======  ================

BattlefieldCode
---------------

:title: Battlefield code
:type: string
:format: default
:constraints:
    :minLength: 5
    :maxLength: 6
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

CWSAC battle identifier


       
Comment
-------

:title: Comment
:type: string
:format: default





       
Source
------

:title: Source
:type: string
:format: default





       
UnitCode
--------

:title: Unit code
:type: string
:format: default





       

