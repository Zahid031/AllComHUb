#!/bin/sh
set -e  # exit on first error

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Django dev server
exec python manage.py runserver 0.0.0.0:8001
