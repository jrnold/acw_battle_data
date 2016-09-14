######################################
CWSS battle data: principal commanders
######################################

:name: cwss_commanders
:path: cwss_commanders.csv
:format: csv

Principal commanders of the battles in the CWSS database.
Each side in a battle in :doc:`cwss_battles` has one or more commanders.
These commanders are largely the same as those in :doc:`cwsac_commanders` and :doc:`cws2_commanders` with some differences for unknown reasons.

This data was extracted from the CWSS database file ``battle.xml``.



Sources: [CWSS]_


Schema
======



================  =======  ================
BattlefieldCode   string   Battlefield code
belligerent       string   belligerent
commander_number  integer  Commander number
commander         string   Commander ID
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


Number of the commander for each side? This does not indicate relative rank of the commanders, but is to serve as a unique ID of the commander when there are multiple commanders on a side in a battle.


       
commander
---------

:title: Commander ID
:type: string
:format: uuid


Unique commander identifier corresponding to the ``PersonID`` in :doc:`cwss_people`.


       

