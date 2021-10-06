# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from .models import EventList


class NewEventForm(forms.Form):
    eventname = forms.CharField(        
      widget=forms.TextInput(
          attrs={
              "placeholder": "Username",
              "class": "form-control"
          }
      ))
    # eventdate = forms.DateField(null=True)
    # predtime = forms.FloatField(max_length=50)
    # emerge = forms.CharField(max_length=50)

    class Meta:
        model = EventList
        # fields = ('eventname', 'eventdate', 'predtime', 'emerge')
        fields = ('eventname')


