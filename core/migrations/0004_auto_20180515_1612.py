# Generated by Django 2.0.5 on 2018-05-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180515_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Nombre del evento'),
        ),
    ]
