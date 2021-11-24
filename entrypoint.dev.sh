#!/bin/bash

set -e

echo "${0}: resetting database."
python manage.py reset_db --noinput

echo "${0}: running migrations."
python manage.py migrate

echo "${0}: loading initial data."
python manage.py loaddata city.json
python manage.py loaddata customer.json

echo "${0}: collecting static files."
python manage.py collectstatic --noinput --clear

echo "${0}: Running development server."
python manage.py runserver 0.0.0.0:8000
