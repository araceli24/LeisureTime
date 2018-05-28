# Generated by Django 2.0.5 on 2018-05-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_event_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_end',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha fin'),
        ),
        migrations.AddField(
            model_name='event',
            name='time_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora fin'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora'),
        ),
    ]
