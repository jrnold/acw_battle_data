#########################
CWSS battle data: battles
#########################

:name: cwss_battles
:path: data/cwss_battles.csv
:format: csv

Battles of the Civil War Soldiers and Sailors (CWSS) database.
These battles are largely the same set as in the CWSAC Report (:doc:`cwsac_battles`) with a few exceptions, some of which appear to be errors.

This data was extracted from the CWSS database file ``battle.xml``.


Sources: [CWSS]_


Schema
======



==================  =======  ====================
BattlefieldCode     string   Battlefield code
BattleName          string   Battle name
BattleType          string   Battle type
BeginDate           date     Begin date
EndDate             date     End date
State               string   State
TheaterCode         string   TheaterCode
CampaignCode        string   CampaignCode
Result              string   Result
TotalCasualties     integer  TotalCasualties
Comment             string   Comment
ID                  integer  ID
ShortSummary        string   Short summary
ShortSummarySource  string   Short summary source
Summary             string   Summary
SummarySource       string   Summary source
URL                 string   URL
==================  =======  ====================

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


       
BattleName
----------

:title: Battle name
:type: string
:format: default





       
BattleType
----------

:title: Battle type
:type: string
:format: default





       
BeginDate
---------

:title: Begin date
:type: date
:format: default





       
EndDate
-------

:title: End date
:type: date
:format: default





       
State
-----

:title: State
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z][A-Z]
    




       
TheaterCode
-----------

:title: TheaterCode
:type: string
:format: default





       
CampaignCode
------------

:title: CampaignCode
:type: string
:format: default





       
Result
------

:title: Result
:type: string
:format: default





       
TotalCasualties
---------------

:title: TotalCasualties
:type: integer
:format: default
:constraints:
    :minimum: 0
    




       
Comment
-------

:title: Comment
:type: string
:format: default





       
ID
--

:title: ID
:type: integer
:format: default





       
ShortSummary
------------

:title: Short summary
:type: string
:format: default





       
ShortSummarySource
------------------

:title: Short summary source
:type: string
:format: default





       
Summary
-------

:title: Summary
:type: string
:format: default





       
SummarySource
-------------

:title: Summary source
:type: string
:format: default





       
URL
---

:title: URL
:type: string
:format: url





       

