#########################################################################
Comparison of battles in CWSAC AAD, CWSAC Report, CWSAC Updates, and CWSS
#########################################################################

:name: nps_battlelist
:path: data/nps_battlelist.csv
:format: csv

List of battles included in the AAD CWSAC Reports (1990-1993), CWSAC Report Battle Summaries (1997), CWSAC Report Updates (2009-2013), and the CWSS. All these reports from the National Park Service use the same battle identifiers, but they differ slightly in their composition.


Sources: [CWSAC1997]_, [CWSAC_AAD]_, [CWSAC_by_state]_, [CWSS]_, [CWSII]_, [CWSIIAL]_, [CWSIIAR]_, [CWSIICO]_, [CWSIIDC]_, [CWSIIFL]_, [CWSIIGA]_, [CWSIIIN]_, [CWSIIKS]_, [CWSIIKY]_, [CWSIILA]_, [CWSIIMD]_, [CWSIIMN]_, [CWSIIMO]_, [CWSIINC]_, [CWSIIND]_, [CWSIIOH]_, [CWSIIOK]_, [CWSIIPA]_, [CWSIISC]_, [CWSIITN]_, [CWSIITX]_, [CWSIIVA]_, [CWSIIWV]_


Schema
======



===========  =======  ===========
cwsac_id     string   cwsac_id
battle_name  string   battle_name
cwss         boolean  cwss
cwsac1       boolean  cwsac1
cws2         boolean  cws2
aad          boolean  aad
notall       boolean  notall
===========  =======  ===========

cwsac_id
--------

:title: cwsac_id
:type: string
:format: default





       
battle_name
-----------

:title: battle_name
:type: string
:format: default





       
cwss
----

:title: cwss
:type: boolean
:format: default





       
cwsac1
------

:title: cwsac1
:type: boolean
:format: default





       
cws2
----

:title: cws2
:type: boolean
:format: default





       
aad
---

:title: aad
:type: boolean
:format: default





       
notall
------

:title: notall
:type: boolean
:format: default





       

