from django.core.management.base import BaseCommand
from django.core.mail import send_mail


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('send email')
        send_mail(
            'That’s your subject',
            'That’s your message body',
            'm7baidak@gmail.com',
            ['m7baidak@gmail.com'],
            fail_silently=False,
        )
        print("That`s allright")

