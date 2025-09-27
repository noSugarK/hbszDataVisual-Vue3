#!/bin/bash
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py init
python apps/account/generate_keys.py
daphne -b 0.0.0.0 -p 8000 --proxy-headers backend.asgi:application
