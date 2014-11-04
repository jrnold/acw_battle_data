#!/bin/bash
ENGINE=sqlite:///acwbdb.sqlite3
PYTHON=python3
DATADIR=./data

$PYTHON scripts/initdb.py $ENGINE
$PYTHON scripts/misc.py $ENGINE $DATADIR
$PYTHON scripts/cwsac.py $ENGINE $DATADIR
# $PYTHON scripts/cwsac2.py $ENGINE $DATADIR
# $PYTHON scripts/livermore.py $ENGINE $DATADIR
# $PYTHON scripts/phister.py $ENGINE $DATADIR
