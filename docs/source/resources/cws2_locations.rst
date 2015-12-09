###########################################
CWSAC Report Updates battle data: locations
###########################################

:name: cws2_locations
:path: data/cws2_locations.csv
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



========  ======  ==============
battle    string  Battle
state     string  State
location  string  County or City
========  ======  ==============

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


       
state
-----

:title: State
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z][A-Z]
    

2-letter State abbreviation


       
location
--------

:title: County or City
:type: string
:format: default


County or city in which the battle occurred.


       

