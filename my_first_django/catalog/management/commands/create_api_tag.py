from django.core.management.base import BaseCommand
from catalog.models import Tag
import requests


class Command(BaseCommand):


    def handle(self, *args, **options):
        API = "http://127.0.0.1:8000/api/tag/"
        r = requests.get(API)
        print(r.status_code)
        print(r)
        req = requests.post(API, data={'name': 'custom api tag'})
        print(req.status_code)




