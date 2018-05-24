from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import EventForm, PlaceForm
from .models import Event, Place
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView, FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .filters import EventFilter

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Create your views here.

# class SearchView(FilterView):
#     template_name = "events/event_list.html"
#     context_object_name = 'events'
#     model = Event
#     filterset_class = filters.EventFilter

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         category = self.request.GET.get('category')
#         if category != None: 
#             queryset = queryset.filter(category=category)
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


class EventListView(ListView):
    model = Event
    queryset = Event.objects.all()
    template_name = "events/event_list.html"
    context_object_name= 'events'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category != None: 
            queryset = queryset.filter(category=category)
                
                    
        return queryset

def event_search(request):
    event_list = Event.objects.all()
    event_filter = EventFilter(request.GET, queryset = event_list)
    return render(request, 'core/event_search.html', {'filter' : event_filter})

class PlaceListView(ListView):
	model = Place
	queryset = Place.objects.all()
	template_name = "places/event_list.html"


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('events_list')

class EventUpdate(UpdateView):
    model = Event
    fields = ['user','title', 'date','time', 'description', 'category', 'place' , 'price' ,'image']
    template_name = 'core/event_new.html'
    success_url = reverse_lazy('events_list')

class EventCreate(CreateView):
    model = Event
    fields = ['user','title', 'date','time', 'description', 'category', 'place' , 'price' ,'image']
    
    template_name = 'core/event_new.html'
    success_url = reverse_lazy('events_list')
    form = EventForm

class PlaceCreate(CreateView):
    model = Place
    fields = ['name', 'address', 'council', 'district']
    template_name = 'core/place_new.html'
    success_url = reverse_lazy('events_list')
    form = PlaceForm

class EventDetail(DetailView):

    template_name = "core/event_detail.html"
    model = Event

class Login(LoginView):

    def form_valid(self, form):
    
        context= super() .form_valid(form)
        # check in
        return context


# def contact(request):
#     return render(request, 'contact.html')

