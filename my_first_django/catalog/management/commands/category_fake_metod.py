from django.core.management.base import BaseCommand
from catalog.models import Category
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help_text = 'fill db to Category'



    def handle(self, *args, **options):
        list_of_categories = ['notebooks', 'mobiles', 'tvs', 'computer', 'kitchen', 'photocameras', 'videocameras',
                              'instruments']
        for item in list_of_categories:
            Category.objects.create(name=item, description=item)

    print("Category is created")
