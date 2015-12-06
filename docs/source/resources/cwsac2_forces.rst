CWSAC Report Updates battle data: force strengths
================================================================================

:name: cwsac2_forces
:path: data/cwsac2_forces.csv
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



       

description
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Description
:type: string
:format: default 


Description of the units involved
       

strength
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: strength
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Total personnel in the force. In some cases CWSAC gives a numeric value of the forces involved. In other cases, it describes the units involved. The columns ``strength_mean`` and ``strength_var`` estimate the strength combining all information given by CWSAC.
       

regiments
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Regiments
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of regiments
       

companies
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: companies
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of companies
       

brigades
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: brigades
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of brigades
       

divisions
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: divisions
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of divisions
       

corps
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: corps
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of corps
       

armies
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: armies
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of armies
       

cavalry_regiments
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Cavalry Regiments
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of cavalry regiments
       

cavalry_brigades
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Cavalry Brigades
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of cavalry brigades
       

cavalry_divisions
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Cavalry Divisions
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of cavalry divisions
       

cavalry_corps
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Cavalry Corps
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of cavalry corps
       

cavalry_companies
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Cavalry Companies
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of cavalry companies
       

artillery_batteries
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Artillery Batteries
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of artillery batteries
       

artillery_companies
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Artillery Companies
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of artillery companies
       

artillery_regiments
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Artillery Regiments
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of artillery regiments
       

artillery_sections
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Artillery Sections
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of artillery sections
       

infantry_regiments
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Infantry Regiments
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of infantry regiments
       

strength_other
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength (other)
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of personnel involved other than the units listed in the description.
       

ships
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Ships
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of ships involved in the battle
       

guns
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Guns
:type: integer
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Number of artillery pieces involved in the battle
       

strength_mean
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength (mean)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Mean of the estimated strength in personnel of the force. See code for how it is calculated.
       

strength_var
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:title: Strength (variance)
:type: number
:format: default 
:constraints:
    
    
    
    
    
    :minimum: 0 
    
         


Variance of the estimated strength in personnel of the force. See code for how it is calculated.
       

