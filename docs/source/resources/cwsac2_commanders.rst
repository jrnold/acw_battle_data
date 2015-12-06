CWSAC Report Updates: commanders
================================================================================

:name: cwsac2_commanders
:path: data/cwsac2_commanders.csv
:format: csv




Schema
-------





battle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Battle
:type: string
:format: default 
:constraints:
    
    :minLength: 5 
    :maxLength: 6 
    
    :pattern: [A-Z]{2}[0-9]{3}[A-Z]? 
    
    
         


CWSAC battle identifier
       

belligerent
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: belligerent
:type: string
:format: default 
:constraints:
    
    
    
    
    
    
    
    :enum: ['US', 'Confederate', 'Native American']      



       

fullname
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Full name
:type: string
:format: default 



       

rank
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Rank
:type: string
:format: default 


Rank of the commander at the time of the battle
       

last_name
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Last Name
:type: string
:format: default 



       

first_name
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: First Name
:type: string
:format: default 



       

middle_name
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Middle Name
:type: string
:format: default 



       

suffix
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Suffix
:type: string
:format: default 



       

