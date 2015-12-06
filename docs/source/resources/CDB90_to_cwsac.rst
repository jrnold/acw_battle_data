CDB90 to CWSAC battle links
================================================================================

:name: CDB90_to_cwsac
:path: data/CDB90_to_cwsac.csv
:format: csv




Schema
-------





isqno
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: isqno
:type: integer
:format: default 


CDB90 battle sequence number
       

cwsac_id
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: CWSAC Battle Id.
:type: string
:format: default 



       

relation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: relation
:type: string
:format: default 
:constraints:
    
    
    
    
    
    
    
    :enum: ['<', '>', '=']      


Relationship of the CDB90 battle to the CWSAC battle. They can be the same, or one can be a subset of the other.
       

