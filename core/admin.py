from django.contrib import admin
from .models import Place, Event

# from core import models
# Register your models here.

admin.site.register(Place)
admin.site.register(Event)

class PlaceAdmin(admin.ModelAdmin):
    fields = ('name', 'address')