#########
NPS Units
#########

:name: nps_units
:path: nps_units.csv
:format: csv



Sources: 


Schema
======



=========  ======  =========
unit_code  string  unit_code
unit_name  string  unit_name
side       string  side
state      string  state
ordinal    string  ordinal
type       string  type
func       string  func
special    string  special
ethnic     string  ethnic
duplicate  number  duplicate
=========  ======  =========

unit_code
---------

:title: unit_code
:type: string
:format: default





       
unit_name
---------

:title: unit_name
:type: string
:format: default


Unit name.


       
side
----

:title: side
:type: string
:format: default





       
state
-----

:title: state
:type: string
:format: default
:constraints:
    :minLength: 2
    :maxLength: 2
    :pattern: [A-Z]{2}
    




       
ordinal
-------

:title: ordinal
:type: string
:format: default


Unit number.
For example, for the Massachussets 1st Infantry Regiment, the value of ``ordinal`` is 1.


       
type
----

:title: type
:type: string
:format: default
:constraints:
    :minLength: 1
    :maxLength: 1
    

Unit type: regiment, squadron, battery, company.
See ``nps_unit_categories_type`` for descriptions of the categories in this column..


       
func
----

:title: func
:type: string
:format: default


Unit function. Examples include: "Artillery", "Cavalry", "Infantry".


       
special
-------

:title: special
:type: string
:format: default
:constraints:
    :minLength: 1
    :maxLength: 1
    

Additional category of the unit for special units. Examples include: "Veteran (Non Volunteer)", "State Militia", "Mounted", "Heavy Artillery", "Home Guard".
See ``nps_unit_categories_special`` for descriptions of the categories in this column.


       
ethnic
------

:title: ethnic
:type: string
:format: default
:constraints:
    :minLength: 1
    :maxLength: 1
    

Ethnic type of the unit, if any. The only two ethnic types are colored ("C") and Native American ("I").
See ``nps_unit_categories_ethnic`` for descriptions of the categories in this column.


       
duplicate
---------

:title: duplicate
:type: number
:format: default


Number to disambiguate units if there are multiple units with the same unit code.


       

