# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_schedule.settings')

# create a Celery instance and configure it using the settings from Django
app = Celery('task_schedule',broker='redis://127.0.0.1:6379')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-email-task-crontab': {
        'task': 'task_app.tasks.send_email_task',
        'schedule': 60.0, #crontab(hour=7, minute=30, day_of_week=1),
    },
}