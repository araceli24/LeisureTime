# Generated by Django 2.0.5 on 2018-05-31 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_delete_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True),
        ),
    ]
