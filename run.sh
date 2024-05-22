#!/bin/bash

exec poetry run python postgres/create_db.py &
exec poetry run python wsgi.py