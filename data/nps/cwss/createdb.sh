#!/bin/bash
DB=nps_cwss.sqlite3
DIR=csv
SQLITE=sqlite3
#CSVSQL=csvsql

if [ -e "$DB" ]
then
    echo "Deleting $DB"
    rm $DB
fi

echo "Creating $DB and adding schema"
$SQLITE $DB < schema.sql

tables=$($SQLITE $DB .tables)
for tbl in $tables
do
    echo "Loading table $tbl into $DB"
    #$CSVSQL --tabs --insert --no-create -v --db "sqlite:///$DB" $DIR/${tbl}.csv
    $SQLITE $DB <<EOF
.mode tabs
.headers on
.import $DIR/${tbl}.csv $tbl
EOF
done
