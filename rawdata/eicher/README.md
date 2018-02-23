Data from John H. Eicher and David J. Eicher "Civil War High Commands"


# abbrev.tsv

"Abbreviations, Acronyms, Symbols and Military Lexicon", p. xxiii--xxv.

Note that abbreviations to meanings is many-to-many. Some abbreviations have
multiple meanings, e.g. "U.S.A", "C.S.A", "d.", "m.". And multiple abbreviations
can map to the same meaning.

```yaml
schema:
  fields:
  - name: abbrev
    type: string
    label: Abbreviation
  - name: meaning
    type: string
    label: Meaning
  - name: note
    type: string
    label: Note
    description: Additional information about the abbreviation.
  key:
  - abbrev
  - meaning
```

# navy_ship_totals.tsv

From p. 18. The composoition of navy forces (number of ships) from 1861--1868.

# Possible Data

## Staff Commands of US and Confederate Armies and Navies

## US Army Military Divisions Departments and Districts

On p. 819

- Department

  - alternative name
  - note on the area
  - predecessor unit
  - successor unit
  - commanders

    - name
    - assigned date
    - assumed date
    - end date
    - was assignment revoked and date
    - temporary
    - never assumed command

## US Army Armies and Army Corps

- army/corps

  - name
  - commanders
    - name
    - start date
    - end date

  - note

## US Navy Squadrons and Flotillas and their commanders

- name
  - commanders
    - name
    - start date
    - end-date
    - temporary
  - note
  - prewar/suspended


# Confederate States Principal Geographic units

- Departmentk
  - Name
  - Alterntive name
  - commanders

    - name
    - start date
    - assumed date
    - end date
    - temporary
    - surrendered

  - note

# Confederate States Principal Armies and Army Corps

- Army/corps

  - name
  - alternative names
  - commanders
    - name
    - start date
    - end date
    - temporary
    - assumed date
    - surrendered
    - official date
  - notes

# Confederate States Princiapl Navy Squadrons and their Commanders

- Squadron

  - name
  - location
  - commanders

    - name
    - start date
