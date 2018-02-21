#!/bin/bash
PORT=${PORT:-5000}
gunicorn prombench.api.wsgi:app -b :$PORT --timeout 120 -w 4 --reload -c conf/gunicorn.py
