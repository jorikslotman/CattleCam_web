#!/bin/sh

SET -e
python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
uwsgi --socket :8000 --master --enable-threads --module cattleweb.wsgi