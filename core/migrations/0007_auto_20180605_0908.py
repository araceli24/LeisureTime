# Generated by Django 2.0.6 on 2018-06-05 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180601_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
