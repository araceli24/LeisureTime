from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.event_list, name='event_list'),
]