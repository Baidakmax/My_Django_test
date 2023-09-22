from celery import shared_task
from my_first_django.celery import app as celery_app
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


@celery_app.task(name="send_message")
def emailing():
    send_mail(
        'Welcome to',
        '<br>Дякую за реестрацію</br>',
        'm7baidak@gmail.com',
        ['m7baidak87@gmail.com'],
        fail_silently=False,
    )
    logger.info('email send')
    logger.warning('email send')
    logger.critical('email send')