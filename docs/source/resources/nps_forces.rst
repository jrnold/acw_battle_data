#####################################
NPS combined data battle data: forces
#####################################

:name: nps_forces
:path: nps_forces.csv
:format: csv

Force level data combining the National Park Services reports: Shenandoah, preliminary CWSAC reports in the AAD (1990-1993), CWSAC Report battle summaries (1997), Civil War Soldiers and Sailors (CWSS) database, and the CWSAC Report Updates (2009-2013).

For each of the casualty types and strength a mean and variance is provided. The values of casualties come from the CWSS, and CWSAC reports, in that order of preference.
The values of strength come from the CWSS, CWSAC II, and CWSAC reports, in that order of preference.

- mean: the given value, or the midpoint if a range is given.
- variance:

   - If a range is given, the variance of a uniform distribution with that range.
   - If no range is given, the measurement error implied by rounding. :math:`var(x) = \frac{1}{12} 10^k`, where :math:`k` is the number of zeros in the value.


Sources: 


Schema
======



============  ======  ==============================
cwsac_id      string  CWSAC Id.
belligerent   string  belligerent
cas_kwm_mean  number  Casualties (mean)
cas_k_mean    number  Killed (mean)
cas_w_mean    number  Wounded (mean)
cas_m_mean    number  Missing or captured (mean)
cas_kwm_var   number  Casualties (variance)
cas_k_var     number  Killed (variance)
cas_w_var     number  Wounded (variance)
cas_m_var     number  Missing or captured (variance)
cas_kw_mean   number  Killed or wounded (mean)
cas_kw_var    number  Killed or wounded (variance)
str_mean      number  Personnel (mean)
str_var       number  Personnel (variance)
cas_km_mean   number  Killed or missing (mean)
cas_wm_mean   number  Wounded or missing (mean)
cas_km_var    number  Killed or missing (variance)
cas_wm_var    number  Wounded or missing (variance)
============  ======  ==============================

cwsac_id
--------

:title: CWSAC Id.
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
    

Side of the force: Confederate or Union or Native American.


       
cas_kwm_mean
------------

:title: Casualties (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Number of casualties (killed, wounded, or missing). Mean estimate.


       
cas_k_mean
----------

:title: Killed (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Number killed. Mean estimate.


       
cas_w_mean
----------

:title: Wounded (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Number wounded. Mean estimate.


       
cas_m_mean
----------

:title: Missing or captured (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Number missing or captured. Mean estimate.


       
cas_kwm_var
-----------

:title: Casualties (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Number of casualties (killed, wounded, or missing). Variance of estimate.


       
cas_k_var
---------

:title: Killed (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Number killed. Variance of estimate.


       
cas_w_var
---------

:title: Wounded (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Number killed. Variance of estimate.


       
cas_m_var
---------

:title: Missing or captured (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    

Number missing or captured. Variance of estimate.


       
cas_kw_mean
-----------

:title: Killed or wounded (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
cas_kw_var
----------

:title: Killed or wounded (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
str_mean
--------

:title: Personnel (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
str_var
-------

:title: Personnel (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
cas_km_mean
-----------

:title: Killed or missing (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
cas_wm_mean
-----------

:title: Wounded or missing (mean)
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
cas_km_var
----------

:title: Killed or missing (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    




       
cas_wm_var
----------

:title: Wounded or missing (variance)
:type: number
:format: default
:constraints:
    :minimum: 0
    




       

