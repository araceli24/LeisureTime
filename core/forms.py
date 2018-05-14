from django import forms
from django.forms import ModelForm, SelectMultiple, TextInput, Textarea
from .models import Event, Place
from django.contrib.auth.models import User


class TimeSelectMultiple(SelectMultiple):
    template_name = 'forms/timeselect.html'



class EventForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=TimeSelectMultiple)

    class Meta:
        model = Event
        fields = ['user', 'date', 'title', 'description', 'place', 'image']
         