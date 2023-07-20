from django.core.management.base import BaseCommand
from catalog.models import Tag
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help_text = 'fill db to Tags'

    def handle(self, *args, **options):
        for _ in range(10):
            Tag.objects.create(name=fake.first_name())

    print("Tags is created")

