from django.contrib import admin
from .models import Place, Event

from core import models
# Register your models here.

# admin.site.register(Place)
# admin.site.register(Event)
# admin.site.register(Category)
# admin.site.register(Organism)
# class OrganismAdmin(admin.ModelAdmin):
#     fields = ( 'name', 'owner')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = models.Place
    fields = ('name', 'address', 'council', 'district')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    fields = ('user', 'date', 'time', 'title', 'description', 'category', 'place' , 'price' ,'image')

