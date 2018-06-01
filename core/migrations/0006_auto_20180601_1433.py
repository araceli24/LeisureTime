# Generated by Django 2.0.5 on 2018-06-01 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180601_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.TextField(choices=[('ARTE', 'Arte'), ('CULTURA', 'Cultura'), ('DEPORTE', 'Deporte'), ('GASTRONOMÍA', 'Gastronomía'), ('MÚSICA', 'Música'), ('OTRO', 'Otro')], default='CULTURA', verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Place', verbose_name='Lugar'),
        ),
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Administrador'),
        ),
    ]
