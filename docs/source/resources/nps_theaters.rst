#######################################
NPS combined data battle data: theaters
#######################################

:name: nps_theaters
:path: nps_theaters.csv
:format: csv

Theaters in the National Park Services reports: Shenandoah, preliminary CWSAC reports in the AAD (1990-1993), CWSAC Report battle summaries (1997), Civil War Soldiers and Sailors (CWSS) database, and the CWSAC Report Updates (2009-2013).

This table is the same as the CWSS theaters, :doc:`cwss_theaters`.


Sources: 


Schema
======



=================  ======  ==================
TheaterCode        string  Theater Code
TheaterName        string  Theater Name
WikipediaCategory  string  Wikipedia Category
WikipediaPage      string  Wikipedia Page
=================  ======  ==================

TheaterCode
-----------

:title: Theater Code
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{2}
    

CWSS Theater Code


       
TheaterName
-----------

:title: Theater Name
:type: string
:format: default





       
WikipediaCategory
-----------------

:title: Wikipedia Category
:type: string
:format: default


Title of the English Wikipedia category for the theater.

Sources: 

       
WikipediaPage
-------------

:title: Wikipedia Page
:type: string
:format: default


Title of the English Wikipedia category for the theater.

Sources: 

       

