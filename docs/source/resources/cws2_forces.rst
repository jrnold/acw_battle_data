#################################################
CWSAC Report Updates battle data: force strengths
#################################################

:name: cws2_forces
:path: data/cws2_forces.csv
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



===================  =======  ===================
battle               string   Battle
belligerent          string   belligerent
description          string   Description
strength             integer  strength
regiments            integer  Regiments
companies            integer  companies
brigades             integer  brigades
divisions            integer  divisions
corps                integer  corps
armies               integer  armies
cavalry_regiments    integer  Cavalry Regiments
cavalry_brigades     integer  Cavalry Brigades
cavalry_divisions    integer  Cavalry Divisions
cavalry_corps        integer  Cavalry Corps
cavalry_companies    integer  Cavalry Companies
artillery_batteries  integer  Artillery Batteries
artillery_companies  integer  Artillery Companies
artillery_regiments  integer  Artillery Regiments
artillery_sections   integer  Artillery Sections
infantry_regiments   integer  Infantry Regiments
strength_other       integer  Strength (other)
ships                integer  Ships
guns                 integer  Guns
strength_mean        number   Strength (mean)
strength_var         number   Strength (variance)
===================  =======  ===================

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
    




       
description
-----------

:title: Description
:type: string
:format: default


Description of the units involved


       
strength
--------

:title: strength
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Total personnel in the force. In some cases CWSAC gives a numeric value of the forces involved. In other cases, it describes the units involved. The columns ``strength_mean`` and ``strength_var`` estimate the strength combining all information given by CWSAC.


       
regiments
---------

:title: Regiments
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of regiments


       
companies
---------

:title: companies
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of companies


       
brigades
--------

:title: brigades
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of brigades


       
divisions
---------

:title: divisions
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of divisions


       
corps
-----

:title: corps
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of corps


       
armies
------

:title: armies
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of armies


       
cavalry_regiments
-----------------

:title: Cavalry Regiments
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of cavalry regiments


       
cavalry_brigades
----------------

:title: Cavalry Brigades
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of cavalry brigades


       
cavalry_divisions
-----------------

:title: Cavalry Divisions
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of cavalry divisions


       
cavalry_corps
-------------

:title: Cavalry Corps
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of cavalry corps


       
cavalry_companies
-----------------

:title: Cavalry Companies
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of cavalry companies


       
artillery_batteries
-------------------

:title: Artillery Batteries
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of artillery batteries


       
artillery_companies
-------------------

:title: Artillery Companies
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of artillery companies


       
artillery_regiments
-------------------

:title: Artillery Regiments
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of artillery regiments


       
artillery_sections
------------------

:title: Artillery Sections
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of artillery sections


       
infantry_regiments
------------------

:title: Infantry Regiments
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of infantry regiments


       
strength_other
--------------

:title: Strength (other)
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of personnel involved other than the units listed in the description.


       
ships
-----

:title: Ships
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of ships involved in the battle


       
guns
----

:title: Guns
:type: integer
:format: default
:constraints:
    :minimum: 0
    

Number of artillery pieces involved in the battle


       
strength_mean
-------------

:title: Strength (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Mean of the estimated strength in personnel of the force. See code for how it is calculated.

**Sources:**
- jrnold; jeffrey.arnold@gmail.com

       
strength_var
------------

:title: Strength (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Variance of the estimated strength in personnel of the force. See code for how it is calculated.

**Sources:**
- jrnold; jeffrey.arnold@gmail.com

       

