# gunicorn config

bind = '0.0.0.0:9980'
workers = 4
timeout = 600
debug = False
capture_output = True
preload_app = True

