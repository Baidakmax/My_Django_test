from django.db import models
from ckeditor.fields import RichTextField
import uuid
# Create your models here.

class TimeDateBaseModel:
    create = models.DateTimeField("Create", auto_now_add=True, null=True, editable=False)
    update = models.DateTimeField("Update", auto_now=True, null=True, editable=False)

    class Meta:
        abstract: True


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('name', max_length=20, unique=True)
    description = RichTextField('Description', default='')
    image = models.ImageField(upload_to='image', null=True, blank=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField('Товари', max_length=20)
    description = RichTextField('Опис')
    price = models.FloatField('Ціна $')
    active = models.BooleanField('В наявності', default=False, help_text='показувати чи не показувати товар')
    country = models.CharField('Країна виробник', max_length=25, default="країна")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods', default=True)
    tags = models.ManyToManyField(Tag, related_name='goods_tag', default=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}, ціна: {self.price}"



