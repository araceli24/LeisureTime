from django.conf.urls import include, url
from django.urls import path, re_path
from . import views
from core.views import EventDetail

urlpatterns = [
    
    path('', views.EventListView.as_view(), name='events_list'),
    path('search/', views.EventSearch.as_view(),  name='search'),
    path('event/expired/', views.EventListViewExpired.as_view(),  name='event_expired'),
    path('event/new', views.EventCreate.as_view(), name='event_new'),
    path('place/new', views.PlaceCreate.as_view(), name='place_new'),
    re_path(r'^event/(?P<pk>\d+)/delete/$', views.EventDelete.as_view(), name='event_delete'),
    re_path(r'^event/(?P<pk>\d+)/edit/$', views.EventUpdate.as_view(), name='event_edit'),
    path('mapa', views.Map.as_view(), name='map'),
    re_path(r'^event/(?P<pk>\d+)/$', views.EventDetail.as_view(), name='event_detail'),
  
]