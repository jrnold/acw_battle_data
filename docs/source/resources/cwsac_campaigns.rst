###################################
CWSAC Report battle data: campaigns
###################################

:name: cwsac_campaigns
:path: cwsac_campaigns.csv
:format: csv



Sources: [CWSAC1993]_, [CWSAC1997]_, [CWSAC_by_state]_, [CWSAC_by_campgn]_


Schema
======



===========  =======  ===========
campaign     string   Campaign
theater      string   Theater
start_year   integer  Start year
start_month  integer  Start month
end_year     integer  End year
end_month    integer  End Month
dbpedia      string   dbpedia
===========  =======  ===========

campaign
--------

:title: Campaign
:type: string
:format: default


Campaign name


       
theater
-------

:title: Theater
:type: string
:format: default


Theater of the campaign


       
start_year
----------

:title: Start year
:type: integer
:format: default
:constraints:
    :minimum: 1861
    :maximum: 1865
    




       
start_month
-----------

:title: Start month
:type: integer
:format: default
:constraints:
    :minimum: 1
    :maximum: 12
    




       
end_year
--------

:title: End year
:type: integer
:format: default
:constraints:
    :minimum: 1861
    :maximum: 1865
    




       
end_month
---------

:title: End Month
:type: integer
:format: default
:constraints:
    :minimum: 1
    :maximum: 12
    




       
dbpedia
-------

:title: dbpedia
:type: string
:format: default


URI of the dbpedia.org resource for the campaign

Sources: [CWSAC1993]_, [CWSAC1997]_, [CWSAC_by_state]_, [CWSAC_by_campgn]_

       

