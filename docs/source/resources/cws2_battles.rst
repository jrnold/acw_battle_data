#########################################
CWSAC Report Updates battle data: battles
#########################################

:name: cws2_battles
:path: data/cws2_battles.csv
:format: csv



**Sources:**

- CWSII

- CWSIIAL

- CWSIIAR

- CWSIICO

- CWSIIDC

- CWSIIFL

- CWSIIGA

- CWSIIKS

- CWSIIKY

- CWSIIMN

- CWSIILA

- CWSIIMD

- CWSIIMO

- CWSIINC

- CWSIIND

- CWSIIOH

- CWSIIOK

- CWSIIPA

- CWSIISC

- CWSIITN

- CWSIIVA

- CWSIIWV

Schema
======

--------------  -------  -------------------
battle          string   Battle
battle_name     string   Battle Name
state           string   State
campaign        string   Campaign
url             string   url
forces_text     string   Forces
strength        integer  Strength
results_text    string   Results (text)
result          number   result
study_area      number   Study Area
core_area       number   core_area
potnr_boundary  number   potnr_boundary
strength_mean   number   Strength (mean)
strength_var    number   Strength (variance)
--------------  -------  -------------------

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


       
battle_name
-----------

:title: Battle Name
:type: string
:format: default





       
state
-----

:title: State
:type: string
:format: default
:constraints:
    
    :minLength: 2
    :maxLength: 2
    
    :pattern: [A-Z][A-Z]
    
    
         


State in which the battle occurred. Two-letter abbreviation of the state.


       
campaign
--------

:title: Campaign
:type: string
:format: default


Campaign of the battle


       
url
---

:title: url
:type: string
:format: url


URL of the CWSAC Updated report


       
forces_text
-----------

:title: Forces
:type: string
:format: default


Text description of the forces involved in the battle


       
strength
--------

:title: Strength
:type: integer
:format: default
:constraints:
    
    
    
    
    
    :minimum: 0
    
         


Total personnel (on both sides) in the battle. For some battles, CWSAC gives an aggregate total, but not totals for the individual sides.


       
results_text
------------

:title: Results (text)
:type: string
:format: default


Description of the result of the battle


       
result
------

:title: result
:type: number
:format: default


Battle result


       
study_area
----------

:title: Study Area
:type: number
:format: default


Study area in acres
The Study Area represents the historic extent of the battle as it unfolded across the landscape. The Study Area contains resources known to relate to or contribute to the battle event: where troops maneuvered and deployed, immediately before and after combat, and where they fought during combat. Historic accounts, terrain analysis, and feature identification inform the delineation of the Study Area boundary.  Historic setting, approaches, and natural features that figure importantly in the battle are defining elements. The Study Area indicates the extent to which historic and archeological resources associated with the battle (areas of combat, command, communications, logistics, medical services, etc.) may be found and protected. Surveyors delineated Study Area boundaries for every battle site that was positively identified through research and field survey, regardless of its present integrity.


       
core_area
---------

:title: core_area
:type: number
:format: default


Core area in acres
The Core Area represents the areas of direct engagement on the battlefield. Positions that delivered or received fire, and the space connecting them, fall within the Core Area.  Frequently described as “hallowed ground,” land within the Core Area is often the first to be targeted for protection. There may be more than one Core Area on a battlefield, but all lie within the Study Area.


       
potnr_boundary
--------------

:title: potnr_boundary
:type: number
:format: default


Potential National Register Boundary area in acres
Unlike the Study and Core Area, which are based only upon the interpretation of historic events, the Potential National Register (PotNR) boundary represents ABPP’s assessment of a Study Area’s current integrity (the surviving landscape and features that convey the site’s historic sense of place). The PotNR boundary may include all or some of the Study Area, and all or some of the Core Area. Although preparing a National Register nomination may require further assessment of historic integrity and more documentation than that provided by the ABPP survey, PotNR boundaries identify land that merits this additional effort.


       
strength_mean
-------------

:title: Strength (mean)
:type: number
:format: default
:constraints:
    
    
    
    
    
    :minimum: 0
    
         


Mean of the estimated strength in personnel of the force. See code for how it is calculated.

**Sources:**
- CWSII
- CWSIIAL
- CWSIIAR
- CWSIICO
- CWSIIDC
- CWSIIFL
- CWSIIGA
- CWSIIKS
- CWSIIKY
- CWSIIMN
- CWSIILA
- CWSIIMD
- CWSIIMO
- CWSIINC
- CWSIIND
- CWSIIOH
- CWSIIOK
- CWSIIPA
- CWSIISC
- CWSIITN
- CWSIIVA
- CWSIIWV

       
strength_var
------------

:title: Strength (variance)
:type: number
:format: default
:constraints:
    
    
    
    
    
    :minimum: 0
    
         


Variance of the estimated strength in personnel of the force. See code for how it is calculated.

**Sources:**
- CWSII
- CWSIIAL
- CWSIIAR
- CWSIICO
- CWSIIDC
- CWSIIFL
- CWSIIGA
- CWSIIKS
- CWSIIKY
- CWSIIMN
- CWSIILA
- CWSIIMD
- CWSIIMO
- CWSIINC
- CWSIIND
- CWSIIOH
- CWSIIOK
- CWSIIPA
- CWSIISC
- CWSIITN
- CWSIIVA
- CWSIIWV

       

