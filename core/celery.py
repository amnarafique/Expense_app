from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

BROKER_URL = 'redis://localhost:6379'
app = Celery('core', broker=BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'users.tasks.pay_salary',
        'schedule': crontab(0, 0, day_of_month='1')
    },
}


app.autodiscover_tasks()