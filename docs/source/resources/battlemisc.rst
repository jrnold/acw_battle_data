#########################
Miscellaneous battle data
#########################

:name: battlemisc
:path: data/battlemisc.csv
:format: csv

Miscellaneous battle data.

Miscellaneous battle-level data coded for this dataset.
The battles are the CWSAC battles (see :doc:`cwsac_battles`).
The extra data includes:

- surrenders
- attackers
  


**Sources:**
- jrnold; jeffrey.arnold@gmail.com


Schema
======



===========  ======  ===========
cwsac_id     string  CWSAC Id.
battle_name  string  Battle name
attacker     string  Attacker
surrender    string  Surrender
===========  ======  ===========

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


       
surrender
---------

:title: Surrender
:type: string
:format: default
:constraints:
    :enum: ['Union complete', 'Union partial', 'None', 'Confederate partial', 'Confederate complete']
    

Did one of the sides surrender?


       

