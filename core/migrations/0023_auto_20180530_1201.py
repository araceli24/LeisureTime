# Generated by Django 2.0.5 on 2018-05-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_map_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.TextField(choices=[('ARTÍSTICO', 'Artístico'), ('CULTURAL', 'Cultural'), ('DEPORTIVO', 'Deportivo'), ('GASTRONÓMICO', 'Gastronómico'), ('MÚSICAL', 'Músical'), ('OTRO', 'Otro')], default='CULTURAL', verbose_name='Tipo'),
        ),
    ]