# Generated by Django 2.0.6 on 2018-06-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180605_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='council',
            field=models.TextField(choices=[('CAMBADOS', 'Cambados'), ('O GROVE', 'O Grove'), ('A ILLA', 'Illa de Arousa'), ('MEAÑO', 'Meaño'), ('MEIS', 'Meis'), ('RIBADUMIA', 'Ribadumia'), ('SANXENXO', 'Sanxenxo'), ('VILAGARCÍA', 'Vilagarcía'), ('VILANOVA', 'Vilanova')], default='MEAÑO', verbose_name='Concello'),
        ),
    ]
