from django.shortcuts import render

# Create your views here.

def event_list(request):
        return render(request, 'core/event_list.html', {})