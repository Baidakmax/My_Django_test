import os
from celery import Celery
import pika


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_django.settings')
app = Celery(broker='amqp://baidakmax:qaz123WSX@localhost:5672', backend='rpc://')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_heartbeat = 0