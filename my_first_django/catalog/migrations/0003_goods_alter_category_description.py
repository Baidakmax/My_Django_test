# Generated by Django 4.2.3 on 2023-07-13 13:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Товари')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Опис')),
                ('price', models.FloatField(verbose_name='Ціна')),
                ('active', models.BooleanField(default=False, help_text='показувати чи не показувати товар', verbose_name='В наявності')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Description'),
        ),
    ]