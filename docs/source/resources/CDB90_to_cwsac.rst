###########################
CDB90 to CWSAC battle links
###########################

:name: CDB90_to_cwsac
:path: data/CDB90_to_cwsac.csv
:format: csv



**Sources:**
- jrnold; jeffrey.arnold@gmail.com
- U.S. Army Concepts Analysis Agency. 1991. “Database of Battles-Version 1990 (computer Diskette).” http://www.dtic.mil/docs/citations/ADM000121.; http://www.dtic.mil/docs/citations/ADM000121
- Staff of the Civil War Sites Advisory Commission. 1997. Report on the Nation’s Civil War Battlefields: Technical Volume iI: Battle Summaries. http://www.nps.gov/abpp/battles/tvii.htm (December 7, 2015).; http://www.nps.gov/abpp/battles/tvii.htm


Schema
======



========  =======  ================
isqno     integer  isqno
cwsac_id  string   CWSAC Battle Id.
relation  string   relation
========  =======  ================

isqno
-----

:title: isqno
:type: integer
:format: default


CDB90 battle sequence number


       
cwsac_id
--------

:title: CWSAC Battle Id.
:type: string
:format: default





       
relation
--------

:title: relation
:type: string
:format: default
:constraints:
    :enum: ['<', '>', '=']
    

Relationship of the CDB90 battle to the CWSAC battle. They can be the same, or one can be a subset of the other.


       

