#!/bin/sh

# Run migrations
python manage.py migrate

# Collect static files (optional)
python manage.py collectstatic 

# Start Django dev server
python manage.py runserver 0.0.0.0:8001
