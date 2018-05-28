from django.contrib import admin
from .models import Place, Event


from core import models
# Register your models here.
admin.site.site_header = 'Leisure'

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    model = models.Place
    fields = ('name', 'address', 'council', 'district', 'position')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    fields = ('user', 'date', 'date_end', 'time', 'time_end', 'duration', 'title', 'description', 'category', 'place' , 'price' ,'image')