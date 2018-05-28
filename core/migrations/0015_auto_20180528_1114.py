# Generated by Django 2.0.5 on 2018-05-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180524_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='creado'),
        ),
        migrations.AddField(
            model_name='event',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='modificado'),
        ),
        migrations.AddField(
            model_name='place',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='creado'),
        ),
        migrations.AddField(
            model_name='place',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='modificado'),
        ),
    ]