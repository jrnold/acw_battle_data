###############
cwss_commanders
###############

:name: cwss_commanders
:path: data/cwss_commanders.csv
:format: csv



**Sources:**
- CWSS


Schema
======

================  =======  ================
BattlefieldCode   string   Battlefield code
belligerent       string   belligerent
commander_number  integer  Commander number
commander         string   Commander
================  =======  ================

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


       
belligerent
-----------

:title: belligerent
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate', 'Native American']
    




       
commander_number
----------------

:title: Commander number
:type: integer
:format: default





       
commander
---------

:title: Commander
:type: string
:format: default





       

