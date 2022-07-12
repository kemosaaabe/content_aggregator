import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('aggregator')
app.config_from_object('django_conf:settings', namespace='CELERY')
app.autodiscover_tasks()

