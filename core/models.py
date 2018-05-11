from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField

# Create your models here.




class Place(models.Model):

    # COUNCIL_CHOICES = (
    #     ('MEAÑO', 'Meaño'),
    #     ('SANXENXO', 'Sanxenxo'),
    #     ('CAMBADOS', 'Cambados'),
    # )


    # DISTRICT_CHOICES = (
    #     ('ADINA', 'Adina'),
    #     ('ARRA', 'Arra'),
    #     ('BORDÓNS', 'Bordóns'),
    #     ('DORRÓN', 'Dorrón'),
    #     ('GONDAR', 'Gondar'),
    #     ('NANTES', 'Nantes'),
    #     ('NOALLA', 'Noalla'),
    #     ('PADRIÑÁN', 'Padriñán'),
    #     ('VILALONGA', 'Vilalonga'),
    #     ('CAMBADOS', 'Cambados'),
    #     ('CASTRELO', 'Castrelo'),
    #     ('CORVILLÓN', 'Corvillón'),
    #     ('OUBIÑA', 'Oubiña'),
    #     ('DENA', 'Dena'),
    #     ('PADRENDA', 'Padrenda'),
    #     ('LORES', 'Lores'),
    #     ('SIMES', 'Simes'),
    #     ('MEAÑO', 'Meaño'),
    #     ('XIL', 'Xil'),
    #     ('COBAS', 'Cobas'),
    # )

    # council = models.TextField('Concello', choices= COUNCIL_CHOICES ,null=False, blank=False)
    # district = models.TextField('Districto', choices= DISTRICT_CHOICES,null=False, blank=False)
    name = models.CharField('Localidad', max_length=100)
    address = models.CharField('Dirección', max_length=100)

    def __str__(self):
        return self.address

class Event(models.Model):

    user = models.ManyToManyField(User)
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    place =  models.ForeignKey(Place, on_delete=models.CASCADE)
    image = VersatileImageField('Image', upload_to='images/' ,null=True, blank=True)

    def __str__(self):
        return self.title

