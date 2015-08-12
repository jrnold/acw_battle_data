# Civil War Sailors and Soldiers Database

Data from the National Park Service's [Civil War Soldiers and Sailors Database](http://www.nps.gov/civilwar/soldiers-and-sailors-database.htm), received by request from the National Park Service.

The original CWSS database consists of several xml files and a MS SQL database.

- `battle.xml`: Battles
- `battleunitlink.xml`: Links military units to battles
- `units.xml`: Units 
- `NPS_BattlefieldParks.csv`: List of parks and the battles associated with those parks.
- [nps_cwss-20121031.bak](https://s3.amazonaws.com/jrnold-nps-cwss/nps_cwss-20121031.bak) The
  MS SQLServer database backup with the CWSS database. This is not stored on c
- `new_cwss_sqlserver_script.sql`: Script generated from the database with its schema.

# XML files to csv files

To create a set of csv files from the `xml` files run
```console
$ python3 cwss_xml_to_csv.py
```
This requires `lxml.
This script creates csv files prefixed `cwss_*` in in the current directory.
It takes the `xml` files and creates tidy tables.

# Database to tsv files or SQLite database

Download the MS SQL database
```console
$ wget https://s3.amazonaws.com/jrnold-nps-cwss/nps_cwss-20121031.bak
```
Restore the backup to a MS SQLServer however you want, I think almost anything will work, but MSSQL is not my thing.

To dump the MS SQL database to tab-separated value (tsv) files:
```console
$ python3 mssql_to_tsv.py ENGINE DST
```
Where `ENGINE` is a valid database engine specification in [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pyodbc). `DST` is the directory in which to dump the tables. It will be created if it does not already exist.
This requires `SQLalchemy`.

Create a new SQLite database from those `tsv` files
```console
$ createdb.sh        
```

