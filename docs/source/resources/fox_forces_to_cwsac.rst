##################################################################
Correspondence between battles in ``fox_forces`` and CWSAC battles
##################################################################

:name: fox_forces_to_cwsac
:path: data/fox_forces_to_cwsac.csv
:format: csv

Correspondence between the observations in the revised Fox battle data (:doc:`fox_forces`) and the battle identifiers used by the National Park Servie CWSAC (e.g. :doc:`cwsac_battles`).


**Sources:**
- Fox, William Freeman. 1898. Regimental Losses in the American Civil War, 1861-1865. A Treatise on the Extent and Nature of the Mortuary Losses in the Union Regiments, with Full and Exhaustive Statistics Compiled from the Official Records on File in the State Military Bureaus and at Washington. Albany Pub. Co. http://books.google.com/books?id=R5YukgAACAAJ.; http://books.google.com/books?id=R5YukgAACAAJ


Schema
======



===========  ======  ===========
belligerent  string  Belligerent
battle_name  string  Battle Name
cwsac_id     string  CWSAC Id.
relation     string  Relation
===========  ======  ===========

belligerent
-----------

:title: Belligerent
:type: string
:format: default





       
battle_name
-----------

:title: Battle Name
:type: string
:format: default


Battle name in the ``fox_forces`` data.


       
cwsac_id
--------

:title: CWSAC Id.
:type: string
:format: default
:constraints:
    :pattern: [A-Z]{3}[0-9]{2}[A-Z]?
    

CWSAC battle identification code.


       
relation
--------

:title: Relation
:type: string
:format: default
:constraints:
    :enum: ['<', '>', '=']
    




       

