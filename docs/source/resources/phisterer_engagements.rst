##################################################
Phisterer (1883) chronological list of engagements
##################################################

:name: phisterer_engagements
:path: data/phisterer_engagements.csv
:format: csv

Phisterer (1883) chronological list of engagements

A list of events on p. 83--212. Phisterer's introduction to the
chronological record is:

   Under the orders of the Surgeon-General of the Army, a work of the
   greatest importance was undertaken and completed by that
   Department, viz., '. The Medical and Surgical History of the War of
   the Rebellion," and great credit is due for the magnificent and
   instructive work to Surgeons-General Wm. A. Hammond
   and J. K. Barnes, U. S. Army;
   Surgeon J. H. Brinton, U. S. Volunteers; Assistant-Surgeons
   (then) J. J. Woodward and George A. Otis, U. S. Army, who were
   directly connected with the work, as well as the members of the
   Medical Department, regulars and volunteers, generally.

   In this work there is a chronological record of engagements, etc.,
   compiled by the Chief Clerk of the Surgical
   Division. Mr. Frederick R.  Sparks, from official sources where
   practicable, from Confederate reports, and from Union and
   Confederate newspapers in other cases, where the statement was not
   obviously false. As full as the record is, it is not complete. In
   preparing it for publication here, several minor engagements were
   added, and others may find omissions as well; nevertheless, this is
   the complete record in existence at present.




**Sources:**
- Phisterer1883; http://books.google.com/books?id=cVNHr_nnLlYC


Schema
======



===========  =======  ===========
id           integer  id
start_date   string   start_date
end_date     date     end_date
monthonly    boolean  monthonly
location     string   Location
state        string   State
description  string   Description
===========  =======  ===========

id
--

:title: id
:type: integer
:format: default


Identifier number. These are the numbers given to the engagements in Phisterer (1883).


       
start_date
----------

:title: start_date
:type: string
:format: default





       
end_date
--------

:title: end_date
:type: date
:format: default





       
monthonly
---------

:title: monthonly
:type: boolean
:format: default


For some engagements only the months, and not the exact days are given. For these the first and last days of the month are used as the start and end dates, and this variable is set to true.


       
location
--------

:title: Location
:type: string
:format: default





       
state
-----

:title: State
:type: string
:format: default
:constraints:
    :pattern: [A-Z][A-Z]
    




       
description
-----------

:title: Description
:type: string
:format: default





       

