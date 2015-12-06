kennedy1997_battles
================================================================================

:name: kennedy1997_battles
:path: data/kennedy1997_battles.csv
:format: csv

Kennedy (1997) battle data

Data from

    Frances H. Kennedy and the Conservation Fund (1998) "The Civil War
    Battlefield Guide", http://books.google.com/books?id=qHObJArDHZMC.

The battles in this source correspond to the CWSAC battles and have use
the same identifiers. However, in a few cases, casualty totals for
several battles are aggregated.

Although Kennedy largely follows the CWSAC battle definitions, there are
a few differences:

-  CWSAC VA075 is split into VA075A and VA075B in Kennedy.
-  Kennedy VA031 includes CWSAC battles VA030, VA031
-  Kennedy VA032 includes CWSAC battles VA033, VA033, VA035
-  Kennedy VA038 includes CWSAC battles VA036, VA037, VA038
-  VA020A (Glendale) and VA020B (White Oak Swamp) are combined into a
   single battle VA020. The revised CWSAC reports also combine VA020A
   and VA020B into VA020.
-  Kenndy VA112 "Battle of St. Mary's Chuch" is VA066 in CWSAC.

Corrections to the casualty data:

-  Kennedy inverted the casualties for US and CS forces for TX005.



Schema
-------





battle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: battle
:type: string
:format: default 



       

name
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: name
:type: string
:format: default 



       

state
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: state
:type: string
:format: default 



       

county
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: county
:type: string
:format: default 



       

start_date
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: start_date
:type: string
:format: default 



       

end_date
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: end_date
:type: string
:format: default 



       

casualties_min
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: casualties_min
:type: number
:format: default 



       

casualties_max
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: casualties_max
:type: number
:format: default 



       

casualties_text
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: casualties_text
:type: string
:format: default 



       

missing
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: missing
:type: number
:format: default 



       

