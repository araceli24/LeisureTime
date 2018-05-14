from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import EventForm
from .models import Event, Place
from django.views.generic import DetailView
# from django.template.loader import render_to_string
# from django.views.generic import TemplateView
# from django.shortcuts import redirect
# from app.form import ContactForm

# Create your views here.

def event_list(request):
        events = Event.objects.all()
        places = Place.objects.all()
       
        return render(request, "core/event_list.html", {'events': events, 'places': places })

class EventDetail(DetailView):

    template_name = "core/event_detail.html"
    model = Event

# class HomeView(TemplateView):
#         template_name = 'home.html'

#         def get_context_data(self, **kwargs):
#                 context = super().get_context_data(**kwargs)
#                 context['contact_form'] = ContactForm()

#                 return context
        
#         def post(self, request, *args, **kwargs):
#                 name = request.POST.get('name')
#                 email = request.POST.get('email')
#                 message = request.POST.get('message')

#                 body = render_to_string(
#                         'email_content.html',{
#                                 'name': name,
#                                 'email': email,
#                                 'message': message,
#                         },
#                 )

#                 return redirect ('home')