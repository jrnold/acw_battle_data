#########################
Miscellaneous battle data
#########################

:name: battlemisc
:path: battlemisc.csv
:format: csv

Miscellaneous battle data.

Miscellaneous battle-level data coded for this dataset.
The battles are the CWSAC battles (see :doc:`cwsac_battles`).
The extra data includes:

- surrenders
- attackers
  


Sources: [jrnold]_


Schema
======



===========  =======  ===========
cwsac_id     string   CWSAC Id.
battle_name  string   Battle name
attacker     string   Attacker
siege        boolean  siege
naval        string   naval
===========  =======  ===========

cwsac_id
--------

:title: CWSAC Id.
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    




       
battle_name
-----------

:title: Battle name
:type: string
:format: default





       
attacker
--------

:title: Attacker
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    

Which side was the attacker in the battle? This was coded as the side which first initiated combat in that battle. It is not a measure of which side was attacking in the campaign. This was coded from the descriptions in the CWSAC and Wikipedia.


       
siege
-----

:title: siege
:type: boolean
:format: default





       
naval
-----

:title: naval
:type: string
:format: default
:constraints:
    :enum: ['Yes', 'No', 'Partial']
    

Was this a naval battles? "Yes" if at least one of the side's forces consisted of only ships, e.g. ship vs. ship battles or ship vs. land fortifications. If "Partial", then land forces were involved on both sides, but ships were part of at least one side's forces. If "No", then no naval forces were involved.


       

