###############
CWSS unit lists
###############

:name: cwss_regiments_units
:path: data/cwss_regiments_units.csv
:format: csv

List of combat units. These are mostly, but not exclusively, regiments, and are the units appearing in battles in :doc:`battleunitlinks`.

This is a modified version of the CWSS database table ``Unitz``.


Sources: 


Schema
======



=========  ======  =========
unit_code  string  unit_code
side       string  Side
state      string  State
ordinal    string  ordinal
arm        string  arm
type       string  Type
special    string  Special
duplicate  number  duplicate
ethnic     string  ethnic
unit_name  string  Unit name
notes      string  Notes
func       string  func
=========  ======  =========

unit_code
---------

:title: unit_code
:type: string
:format: default





       
side
----

:title: Side
:type: string
:format: default
:constraints:
    :enum: ['US', 'Confederate']
    

Side of each force


       
state
-----

:title: State
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z]{2}
    

Home state of the unit. This includes codes for "non-states", e.g. US for US Colored troops, and UR for US Regular Army. See :doc:`cwss_state_names` for the abbreviations.


       
ordinal
-------

:title: ordinal
:type: string
:format: default


Ordinal number of the unit, if any. E.g. 1 for the 1st New York Infantry Regiment.


       
arm
---

:title: arm
:type: string
:format: default


Combat arm of the unit. E.g. cavalry, artillery, infantry. See :doc:`cwss_categories` for the abbrevations.


       
type
----

:title: Type
:type: string
:format: default


Type (size) of the unit. E.g. regiment, company, battalion, squadron. See :doc:`cwss_categories` for the abbreviations.


       
special
-------

:title: Special
:type: string
:format: default


Codes for special units, e.g. Marine, Home Guard, Heavy Artillery, Light Artiller, State.  See :doc:`cwss_categories` for the abbreviations.


       
duplicate
---------

:title: duplicate
:type: number
:format: default





       
ethnic
------

:title: ethnic
:type: string
:format: default


Indicator for "ethnic" units: C if colored, I if Native American. See :doc:`cwss_categories` for the abbreviations.


       
unit_name
---------

:title: Unit name
:type: string
:format: default





       
notes
-----

:title: Notes
:type: string
:format: default





       
func
----

:title: func
:type: string
:format: default


Unit function. This column is practically a duplicate of `arm`; I am unsure of the difference.


       

