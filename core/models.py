from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField
from django.shortcuts import reverse
from .widgets import *
from core.services import generate_unique_file_path
# Create your models here.

class TimeStampedModel(models.Model):
    created= models.DateTimeField('creado', auto_now_add=True, blank=True, null=True)
    modified= models.DateTimeField('modificado', auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

class Place(TimeStampedModel):

    COUNCIL_CHOICES = (
    
        ('CAMBADOS', 'Cambados'),
        ('O GROVE', 'O Grove'),
        ('ILLA DE AROUSA', 'Illa de Arousa'),
        ('MEAÑO', 'Meaño'),
        ('MEIS', 'Meis'),
        ('RIBADUMIA', 'Ribadumia'),
        ('SANXENXO', 'Sanxenxo'),
        ('VILAGARCÍA DE AROUSA', 'Vilagarcía'),
        ('VILANOVA', 'Vilanova'),
    )


    council = models.TextField('Concello', choices= COUNCIL_CHOICES ,default='MEAÑO' ,null=False, blank=False)
    district = models.CharField('Parroquia', max_length=100, null=True, blank=True)
    name = models.CharField('Nome', max_length=100, null=True, blank=True)
    address = models.CharField('Dirección', max_length=250, null=True, blank=True)
    latitude = models.DecimalField(
                max_digits=9, decimal_places=7, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=7, null=True, blank=True)

    def __str__(self):
        return self.name

class Event(TimeStampedModel):

    CATEGORY_CHOICES = (
        ('ARTE', 'Arte'),
        ('CULTURA', 'Cultura'),
        ('DEPORTE', 'Deporte'),
        ('GASTRONOMÍA', 'Gastronomía'),
        ('MÚSICA', 'Música'),
        ('OTRO', 'Otro'),
    )

    DURATION_CHOICES = (
        ('Todo el día', 'Día completo'),
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche','Noche' ),
        ('Fin de semana ', 'Fin de semana'),
        
    )

    user = models.ManyToManyField(User, verbose_name='Administrador')
    date = models.DateField('Fecha')
    date_end= models.DateField('Fecha fin',null=True, blank=True)
    time = models.TimeField('Hora',null=True, blank=True)
    time_end = models.TimeField('Hora fin' ,null=True, blank=True)
    title = models.CharField('Nombre del evento', max_length=100)
    description = models.TextField('Descripción', null=False, blank=False)
    place =  models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Lugar')
    category = models.TextField('Tipo', choices= CATEGORY_CHOICES , default='CULTURA',null=False, blank=False)
    price = models.DecimalField('Precio', max_digits=6, decimal_places=2, null=True, default=None, blank=True)
    image = VersatileImageField('Imagen', upload_to=generate_unique_file_path ,null=True, blank=True)
    duration = models.TextField('Duración', choices= DURATION_CHOICES , null=True, blank=True)
    # slug = models.SlugField(max_length=64, blank=True)

    class Meta:
        ordering = ["date", "time"]

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title