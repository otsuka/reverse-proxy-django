import multiprocessing

bind = '127.0.0.1:8000'

daemon = False

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
max_requests = 1000
timeout = 300
keepalive = 2

reload = False
spew = False
preload_app = True

accesslog = '-'
errorlog = '-'

umask = 0o002
loglevel = 'info'
logconfig = None
proc_name = 'gunicorn'
