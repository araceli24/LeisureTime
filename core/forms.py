from django import forms
from django.forms import ModelForm, SelectMultiple, TextInput, Textarea, SelectDateWidget
from .models import Event, Place
from django.contrib.auth.models import User
from django.contrib.admin import widgets

# class DateInput(forms.DateInput):
#     input_type = 'date'

class TimeSelectMultiple(SelectMultiple):
    template_name = 'forms/timeselect.html'



class EventForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=TimeSelectMultiple)
    #date = forms.DateField(widget=forms.SelectDateWidget())

    # date = forms.DateField(widget=forms.DateInput(
    #     format= '%d/%m/%Y') ,
    #     input_formats=( '%d/%m/%Y', ))

    class Meta:
        model = Event
        fields = ['user', 'date', 'time', 'date_end', 'time_end', 'title', 'description', 'category','price', 'place', 'image']
       
        # widgets = {
        #             'date': DateInput(attrs={'type': 'date'})
        #         }

    def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            self.fields['date'].widget = widgets.AdminDateWidget()
            self.fields['time'].widget = widgets.AdminTimeWidget()

class PlaceForm(forms.ModelForm):
    
    class Meta:
        model = Place
        fields = ['name', 'address', 'council', 'district', 'latitude', 'longitude', ]
