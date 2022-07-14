import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aggregator.settings')

app = Celery('aggregator')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get-news-every-10-minutes': {
        'task': 'main.tasks.get_news_task',
        'schedule': crontab(minute='*/10'),
    },
}

