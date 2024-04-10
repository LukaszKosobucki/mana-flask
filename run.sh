#!/bin/bash

exec python postgres/create_db.py &
exec python wsgi.py