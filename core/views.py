from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import EventForm, PlaceForm
from .models import Event, Place
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.core.paginator import EmptyPage, InvalidPage, Paginator

from django_filters.views import FilterView
from .filters import EventFilter

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
# from django.contrib.sites.shortcuts import get_current_site

from django.utils import timezone

# Create your views here.

class EventListView(ListView):
    # FilterView
    model = Event
    template_name = "events/event_list.html"
    context_object_name= 'events'
    paginate_by=6
    # filterset_class = EventFilter
    
    def get_queryset(self):
        now= timezone.now()
        queryset = Event.objects.all().select_related('place').filter(date__gte=now).order_by('date')
        category = self.request.GET.get('category')
        if category != None: 
            queryset = queryset.filter(category=category)
                
                    
        return queryset

class EventListViewExpired(ListView):
    model = Event
    now= timezone.now()
    queryset = Event.objects.all().select_related('place').filter(date__lt=now).order_by('-date')
    template_name = "core/event_list_expired.html"
    context_object_name= 'events'

   
    

class  EventSearch(FilterView):
    model = Event
    template_name = "core/search.html"
    filterset_class = EventFilter
    context_object_name= 'events'
    
    # def get_context_data(self, *args, **kwargs):
    #     data = super().get_context_data(*args, **kwargs)
    #     aux = self.request.GET.copy()
    #     data['query_get_string'] = aux.urlencode()
    #     return data



class PlaceListView(ListView):
	model = Place
	queryset = Place.objects.all()
	template_name = "places/event_list.html"


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'forms/event_confirm_delete.html'
    success_url = reverse_lazy('events_list')
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['user','title', 'date','time', 'description', 'category', 'place' , 'price' ,'image']
    template_name = 'core/event_new.html'
    success_url = reverse_lazy('events_list')


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['user','title', 'date','time', 'description', 'category', 'place' , 'price' ,'image']
    
    template_name = 'core/event_new.html'
    success_url = reverse_lazy('events_list')
    form = EventForm

class PlaceCreate(LoginRequiredMixin, CreateView):
    model = Place
    fields = ['name', 'address', 'council', 'district', 'latitude', 'longitude']
    template_name = 'core/place_new.html'
    success_url = reverse_lazy('events_list')
    form = PlaceForm

class EventDetail(DetailView):

    template_name = "core/event_detail.html"
    model = Event

class Login(LoginView):

    def form_valid(self, form):
    
        context= super() .form_valid(form)
       
        return context


class Map(ListView):

    model = Event
    template_name = "core/map.html"

    

    def get_queryset(self):
        now= timezone.now()
        queryset = Event.objects.all().select_related('place').filter(date__gte=now).order_by('date')
        category = self.request.GET.get('category')
        if category != None: 
            queryset = queryset.filter(category=category)
                
        return queryset
        

def handler404(request):
    return render(request, "404.html", status=404)

def handler500(request):
    return render(request, "500.html", status=500)