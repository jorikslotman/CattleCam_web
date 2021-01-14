#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate

uwsgi --socket :8000 --master --enable-threads --module cattleweb.wsgi