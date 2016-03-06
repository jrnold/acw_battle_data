##################################################
NPS Shenandoah Report battle data: list of battles
##################################################

:name: shenandoah_battles
:path: shenandoah_battles.csv
:format: csv



Sources: [NPS1992]_


Schema
======



=============  =======  =============
battle_number  integer  Battle Number
battle_name    string   Battle Name
cwsac_id       string   cwsac_id
start_date     date     Start Date
end_date       date     End Eate
campaign       string   Campaign
county         string   County
url            string   url
=============  =======  =============

battle_number
-------------

:title: Battle Number
:type: integer
:format: default


Unique identifier in the Shenandoah data.


       
battle_name
-----------

:title: Battle Name
:type: string
:format: default





       
cwsac_id
--------

:title: cwsac_id
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]?
    

Identifier of the battle in CWSAC. See :doc:`cwsac_battles`.


       
start_date
----------

:title: Start Date
:type: date
:format: default





       
end_date
--------

:title: End Eate
:type: date
:format: default





       
campaign
--------

:title: Campaign
:type: string
:format: default





       
county
------

:title: County
:type: string
:format: default


County of the battle


       
url
---

:title: url
:type: string
:format: default





       

