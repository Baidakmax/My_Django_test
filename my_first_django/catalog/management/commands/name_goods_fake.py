from django.core.management.base import BaseCommand
from catalog.models import Good
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help_text = 'fill db to Goods'

    def handle(self, *args, **options):
        for _ in range(10):
            Good.objects.create(name=fake.name(), description=fake.company(),
                                price=1200)

    print("Goods is created")

