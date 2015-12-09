##############################################
CWSAC Report Updates battle data: battle dates
##############################################

:name: cws2_dates
:path: data/cws2_dates.csv
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



==========  =======  ==========
battle      string   Battle
spell       integer  Spell
start_date  date     Start Date
end_date    date     End Date
==========  =======  ==========

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


       
spell
-----

:title: Spell
:type: integer
:format: default
:constraints:
    :minimum: 1
    :maximum: 2
    

Spell number of the battle. Only one battle had non-contiguous dates, and two spells.


       
start_date
----------

:title: Start Date
:type: date
:format: default





       
end_date
--------

:title: End Date
:type: date
:format: default





       

