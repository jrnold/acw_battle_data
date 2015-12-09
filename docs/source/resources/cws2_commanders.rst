################################
CWSAC Report Updates: commanders
################################

:name: cws2_commanders
:path: data/cws2_commanders.csv
:format: csv



**Sources:**
- CWSII; http://www.nps.gov/hps/abpp/CWSII/CWSII.htm
- CWSIIAL; http://www.nps.gov/abpp/CWSII/CWSACReportAlabamaUpdate.pdf
- CWSIIAR; http://www.nps.gov/abpp/CWSII/CWSACReportArkansasUpdate.pdf
- CWSIICO; http://www.nps.gov/abpp/CWSII/CWSACReportFarWestUpdate.pdf
- CWSIIDC; http://www.nps.gov/abpp/CWSII/CWSACReportWashingtonDCUpdate.pdf
- CWSIIFL; http://www.nps.gov/abpp/CWSII/CWSACReportFloridaUpdate.pdf
- CWSIIGA; http://www.nps.gov/abpp/CWSII/CWSACReportGeorgiaUpdate.pdf
- CWSIIKS; http://www.nps.gov/abpp/CWSII/CWSACReportKansasUpdate.pdf
- CWSIIKY; http://www.nps.gov/abpp/CWSII/CWSACReportKentuckyUpdate.pdf
- CWSIIMN; http://www.nps.gov/abpp/CWSII/CWSACReportMinnesotaUpdate.pdf
- CWSIILA; http://www.nps.gov/abpp/CWSII/CWSACReportLouisianaUpdate.pdf
- CWSIIMD; http://www.nps.gov/abpp/CWSII/CWSACReportMarylandUpdate.pdf
- CWSIIMO; http://www.nps.gov/abpp/CWSII/CWSACReportMissouriUpdate.pdf
- CWSIINC; http://www.nps.gov/abpp/CWSII/CWSACReportNorthCarolinaUpdate.pdf
- CWSIIND; http://www.nps.gov/abpp/CWSII/CWSACReportNorthDakotaUpdate.pdf
- CWSIIOH; http://www.nps.gov/abpp/CWSII/CWSACReportOhioUpdate.pdf
- CWSIIOK; http://www.nps.gov/abpp/CWSII/CWSACReportOklahomaUpdate.pdf
- CWSIIPA; http://www.nps.gov/abpp/CWSII/CWSACReportPennsylvaniaUpdate.pdf
- CWSIISC; http://www.nps.gov/abpp/CWSII/CWSACReportSouthCarolinaUpdate.pdf
- CWSIITN; http://www.nps.gov/abpp/CWSII/CWSACReportTennesseeUpdate.pdf
- CWSIIVA; http://www.nps.gov/abpp/CWSII/CWSACReportVirginiaUpdate.pdf
- CWSIIWV; http://www.nps.gov/abpp/CWSII/CWSACReportWestVirginiaUpdate.pdf


Schema
======



===========  ======  ===========
battle       string  Battle
belligerent  string  belligerent
fullname     string  Full name
rank         string  Rank
last_name    string  Last Name
first_name   string  First Name
middle_name  string  Middle Name
suffix       string  Suffix
===========  ======  ===========

battle
------

:title: Battle
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
    




       
fullname
--------

:title: Full name
:type: string
:format: default





       
rank
----

:title: Rank
:type: string
:format: default


Rank of the commander at the time of the battle


       
last_name
---------

:title: Last Name
:type: string
:format: default





       
first_name
----------

:title: First Name
:type: string
:format: default





       
middle_name
-----------

:title: Middle Name
:type: string
:format: default





       
suffix
------

:title: Suffix
:type: string
:format: default





       

