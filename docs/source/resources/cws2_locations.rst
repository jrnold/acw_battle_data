###########################################
CWSAC Report Updates battle data: locations
###########################################

:name: cws2_locations
:path: data/cws2_locations.csv
:format: csv



**Sources:**
- CWSII
- CWSIIAL
- CWSIIAR
- CWSIICO
- CWSIIDC
- CWSIIFL
- CWSIIGA
- CWSIIKS
- CWSIIKY
- CWSIIMN
- CWSIILA
- CWSIIMD
- CWSIIMO
- CWSIINC
- CWSIIND
- CWSIIOH
- CWSIIOK
- CWSIIPA
- CWSIISC
- CWSIITN
- CWSIIVA
- CWSIIWV


Schema
======



========  ======  ==============
battle    string  Battle
state     string  State
location  string  County or City
========  ======  ==============

battle
------

:title: Battle
:type: string
:format: default
:constraints:
    :minLength: 5
    :maxLength: 6
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

CWSAC battle identifier


       
state
-----

:title: State
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z][A-Z]
    

2-letter State abbreviation


       
location
--------

:title: County or City
:type: string
:format: default


County or city in which the battle occurred.


       

