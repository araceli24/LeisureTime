from django.contrib import admin
from .models import Place, Event, Map
from django.conf import settings


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

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name', 'latitude', 'longitude',)
        }),
    )

    class Media:
       
            css = {
                'all': (
                    settings.MEDIA_URL + 'css/location_picker.css',
                    )
            }
            js = (
                 'http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
            'http://www.google.com/jsapi?key=' + settings.MAPS_API_KEY,
            settings.MEDIA_URL + 'js/jquery.location_picker.js',
        )