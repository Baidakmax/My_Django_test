# Generated by Django 4.2.3 on 2023-07-19 14:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_good_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='good',
            name='tags',
            field=models.ManyToManyField(related_name='goods_tag', to='catalog.tag'),
        ),
    ]
