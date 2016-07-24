################################################
NPSA Battles to Dbpedia/Wikipedia Correspondence
################################################

:name: nps_battles_to_wiki
:path: nps_battles_to_wiki.csv
:format: csv



Sources: [jrnold]_


Schema
======



===============  ======  ==============
cwsac_id         string  CWSAC Id
dbpedia_uri      url     Dbpedia URI
wikipedia_title  string  Wikipedia Page
relation         string  relation
===============  ======  ==============

cwsac_id
--------

:title: CWSAC Id
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{3}[0-9]{2}
    

CWSAC ID


       
dbpedia_uri
-----------

:title: Dbpedia URI
:type: url
:format: default


URI of the dbepdia resource for the battle.


       
wikipedia_title
---------------

:title: Wikipedia Page
:type: string
:format: default


Title of the English Wikipedia page for the battle.


       
relation
--------

:title: relation
:type: string
:format: default


One of "=" for equality, "<" for a subset of, and ">" for a superevent of.


       

