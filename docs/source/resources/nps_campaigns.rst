########################################
NPS combined data battle data: campaigns
########################################

:name: nps_campaigns
:path: nps_campaigns.csv
:format: csv

Campaigns in the National Park Services Civil War battle data.

These data are a copy of the CWSS campaign list, :doc:`cwss_campaigns`.


Sources: 


Schema
======



=================  ======  ==================
CampaignCode       string  CampaignCode
CampaignName       string  Campaign Name
CampaignDates      string  CampaignDates
CampaignStartDate  string  Start Date
CampaignEndDate    date    End Date
TheaterCode        string  TheaterCode
WikipediaPage      string  Wikipedia Page
WikipediaCategory  string  Wikipedia Category
=================  ======  ==================

CampaignCode
------------

:title: CampaignCode
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}[0-9]{3}
    

CWSS Campaign Code


       
CampaignName
------------

:title: Campaign Name
:type: string
:format: default





       
CampaignDates
-------------

:title: CampaignDates
:type: string
:format: default


Dates of the campaign (as a string)


       
CampaignStartDate
-----------------

:title: Start Date
:type: string
:format: default





       
CampaignEndDate
---------------

:title: End Date
:type: date
:format: default





       
TheaterCode
-----------

:title: TheaterCode
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}
    




       
WikipediaPage
-------------

:title: Wikipedia Page
:type: string
:format: default


Title of the English Wikipedia page for the campaign


       
WikipediaCategory
-----------------

:title: Wikipedia Category
:type: string
:format: default


Title of the English Wikipedia category for the campaign


       

