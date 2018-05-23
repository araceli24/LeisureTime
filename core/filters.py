from core import models

import django_filters
from .models import Event, Place

class EventFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(label='Buscar', method='filter_search')

    class Meta:
        model = Event
        fields = ['category']