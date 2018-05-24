from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField
from geoposition.fields import GeopositionField

# Create your models here.

class Place(models.Model):

    COUNCIL_CHOICES = (
        ('MEAÑO', 'Meaño'),
        ('SANXENXO', 'Sanxenxo'),
        ('CAMBADOS', 'Cambados'),
    )


    DISTRICT_CHOICES = (
        ('ADINA', 'Adina'),
        ('ARRA', 'Arra'),
        ('BORDÓNS', 'Bordóns'),
        ('DORRÓN', 'Dorrón'),
        ('GONDAR', 'Gondar'),
        ('NANTES', 'Nantes'),
        ('NOALLA', 'Noalla'),
        ('PADRIÑÁN', 'Padriñán'),
        ('VILALONGA', 'Vilalonga'),
        ('CAMBADOS', 'Cambados'),
        ('CASTRELO', 'Castrelo'),
        ('CORVILLÓN', 'Corvillón'),
        ('OUBIÑA', 'Oubiña'), 
        ('DENA', 'Dena'),
        ('PADRENDA', 'Padrenda'),
        ('LORES', 'Lores'),
        ('SIMES', 'Simes'),
        ('MEAÑO', 'Meaño'),
        ('XIL', 'Xil'),
        ('COBAS', 'Cobas'),
    )

    council = models.TextField('Concello', choices= COUNCIL_CHOICES ,default='MEAÑO' ,null=False, blank=False)
    district = models.TextField('Parroquia', choices= DISTRICT_CHOICES, default='MEAÑO', null=False, blank=False)
    name = models.CharField('Nombre', max_length=100, null=True, blank=True)
    address = models.CharField('Dirección', max_length=250)
    position = GeopositionField(blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):

    CATEGORY_CHOICES = (
        ('DEPORTIVO', 'Deportivo'),
        ('MÚSICAL', 'Músical'),
        ('CULTURAL', 'Cultural'),
        ('OTRO', 'Otro'),
    )

    user = models.ManyToManyField(User)
    date = models.DateField('Fecha')
    time = models.TimeField('Hora')
    title = models.CharField('Nombre del evento', max_length=100)
    description = models.TextField()
    place =  models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.TextField('Tipo', choices= CATEGORY_CHOICES , default='CULTURAL',null=False, blank=False)
    price = models.DecimalField('Precio', max_digits=6, decimal_places=2, null=True, default=None, blank=True)
    image = VersatileImageField('Imagen', upload_to='images/' ,null=True, blank=True)

    class Meta:
        ordering = ["date", "time"]

    def __str__(self):
        return self.title