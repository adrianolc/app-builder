#!/bin/sh

source .venv/bin/activate
exec gunicorn --bind 0.0.0.0:5000 "api:create_app()" --log-file=-
# exec flask run --host=0.0.0.0 --port=5000