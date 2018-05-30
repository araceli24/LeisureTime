from core import models

import django_filters
from .models import Event, Place

class EventFilter(django_filters.FilterSet):
    
    class Meta:
        model = Event
        fields = {
            'title': ['icontains'],
        }