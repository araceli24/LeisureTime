from django.conf.urls import include, url
from django.urls import path
from . import views
from core.views import EventDetail

urlpatterns = [
    url(r'^$', views.EventListView.as_view(), name='events_list'),

    url(r'^search/$', views.EventSearch.as_view(),  name='search'),
    url(r'^event/passed/$', views.EventListViewPassed.as_view(),  name='event_passed'),

    url(r'^event/(?P<pk>\d+)/$', views.EventDetail.as_view(), name='event_detail'),
    url(r'^event/new/$', views.EventCreate.as_view(), name='event_new'),
    url(r'^place/new/$', views.PlaceCreate.as_view(), name='place_new'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.EventDelete.as_view(), name='event_delete'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.EventUpdate.as_view(), name='event_edit'),
    url(r'^mapa', views.Map.as_view(), name='map'),
    # path('accounts/', include('django.contrib.auth.urls')),



    # path('accounts/login/', views.LoginView.as_view()),
]