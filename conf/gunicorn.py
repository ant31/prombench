import sys
import os
from promsnaps.config import logfile_path



logconfig = logfile_path(debug=False)
bind = 'unix:/tmp/gunicorn_registry.sock'
workers = 2
worker_class = 'gevent'
preload_app = True
