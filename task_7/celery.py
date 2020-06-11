import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_7.settings')

app = Celery('task_7')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'locations.task.print_to_shell',
        'schedule': crontab(minute="*/20"),
    },
}