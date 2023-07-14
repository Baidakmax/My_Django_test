from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField('name', max_length=20, unique=True)
    description = RichTextField('Description', default='')

    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField('Товари', max_length=20)
    description = RichTextField('Опис')
    price = models.FloatField('Ціна $')
    active = models.BooleanField('В наявності', default=False, help_text='показувати чи не показувати товар')
    country = models.CharField('Країна виробник', max_length=25, default="країна")

    def __str__(self):
        return f"{self.name}, ціна: {self.price}"



