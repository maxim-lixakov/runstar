#!/bin/sh

sleep 10

python manage.py createcachetable
python manage.py collectstatic  --noinput

exec "$@"