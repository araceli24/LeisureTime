# Generated by Django 2.0.5 on 2018-06-01 12:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180601_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
