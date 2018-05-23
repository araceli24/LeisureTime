from django.conf.urls import include, url
from django.urls import path
from . import views
from core.views import EventDetail

urlpatterns = [
    url(r'^$', views.EventListView.as_view(), name='events_list'),

    url(r'^$', views.event_search, name='event_search'),

    url(r'^event/(?P<pk>\d+)/$', views.EventDetail.as_view(), name='event_detail'),
    url(r'^event/new/$', views.EventCreate.as_view(), name='event_new'),
    url(r'^place/new/$', views.PlaceCreate.as_view(), name='place_new'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.event_delete, name='event_delete'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.EventUpdate.as_view(), name='event_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
]