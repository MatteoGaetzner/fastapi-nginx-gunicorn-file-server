# gunicorn_conf.py
from multiprocessing import cpu_count

bind = "127.0.0.1:8000"

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/www-matteogatzner/logs/file-server/access.log'
errorlog =  '/home/www-matteogatzner/logs/file-server/error.log'