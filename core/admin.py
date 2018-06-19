from django.contrib import admin
from .models import Place, Event
from django.conf import settings


from core import models
# Register your models here.

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = models.Place
    fields = ('name', 'address', 'council', 'district', 'latitude', 'longitude')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    fields = ('user', 'date', 'date_end', 'time', 'time_end', 'duration', 'title', 'description', 'category', 'place' , 'price' ,'image')
