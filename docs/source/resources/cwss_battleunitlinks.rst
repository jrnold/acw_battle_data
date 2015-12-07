#########################
CWSS units in each battle
#########################

:name: cwss_battleunitlinks
:path: data/cwss_battleunitlinks.csv
:format: csv



**Sources:**
- CWSS


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





       

