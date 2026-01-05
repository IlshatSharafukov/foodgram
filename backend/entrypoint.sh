#!/bin/bash

python manage.py migrate --no-input
python manage.py collectstatic --no-input

if [ ! -f /app/.ingredients_loaded ]; then
    echo "Loading ingredients..."
    python manage.py load_ingredients
    touch /app/.ingredients_loaded
    echo "Ingredients loaded successfully!"
fi

gunicorn --bind 0.0.0.0:8000 foodgram.wsgi
