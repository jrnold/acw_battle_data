################################
CWSS unit category abbreviations
################################

:name: cwss_categories
:path: cwss_categories.csv
:format: csv

Category abbreviations used in :doc:`cwss_units`.

- "SCharacter": Abbreviations used in the :doc:`cwss_units` column ``special``
- "Unitype":  Abbreviations used in the :doc:`cwss_units` column ``type``
- "Function":  Abbreviations used in the :doc:`cwss_units` column ``func``

This is a slightly modified version of the CWSS database table ``Category``.
  


Sources: 


Schema
======



===========  ======  ===========
category     string  category
abbr         string  abbr
description  string  Description
===========  ======  ===========

category
--------

:title: category
:type: string
:format: default
:constraints:
    :enum: ['SCharacter', 'Unittype', 'Function']
    

If "SCharacter", an abbrevation for the column ``special`` (speical units). If "Function", an abbreviation for the column ``function`` (function of the unit). If "Unitype", an abbreviation fo the column ``type`` in :doc:`cwss_regiments_units`.


       
abbr
----

:title: abbr
:type: string
:format: default
:constraints:
    :minLength: 1
    :maxLength: 1
    :pattern: [A-Z0]
    

Abbreviations appearing in columns ``special``, ``function``, and ``type`` of the table :doc:`cwss_regiments_units`.


       
description
-----------

:title: Description
:type: string
:format: default





       

