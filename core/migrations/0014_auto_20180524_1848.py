# Generated by Django 2.0.5 on 2018-05-24 16:48

import core.services
from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180524_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=core.services.generate_unique_file_path, verbose_name='Imagen'),
        ),
    ]