#!/bin/bash

export PGPASSWORD=mypass
export PGHOST=localhost
export PGUSER=postgres
export PGDATABASE=postgres
export PGPORT=5432


psql -f schema.sql
python gen_test_data.py > test.csv
psql -f load.sql
rm test.csv

