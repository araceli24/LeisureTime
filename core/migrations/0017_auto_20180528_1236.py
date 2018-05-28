# Generated by Django 2.0.5 on 2018-05-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20180528_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='district',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Parroquia'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome'),
        ),
    ]
