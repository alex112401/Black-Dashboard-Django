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
          "placeholder": "EX: 會議 專案...",
          "class": "form-control",
          "list": "datalistOptions" ,
          "id": "eventName",
        }
      ))
      
    eventdate = forms.DateField(      
      widget=forms.TextInput(
        attrs={
          "class": "form-control",
          "type": "date",
          "id": "eventDate",
          "value": "2021-09-22"
        }
      ))

    predtime = forms.FloatField(
      widget=forms.TextInput(
        attrs={
          "class": "form-control",
          "type": "number",
          "id": "predTime",
          "value":1, 
          "step": "0.01", 
          "min":"0"
        }
      ))

    CHOICES = (
      ("緊急", "緊急"),
      ("重要", "重要"),
      ("普通", "普通"),
      ("可暫緩", "可暫緩"),
    )
    
    emerge = forms.ChoiceField(
      choices=CHOICES,
      widget=forms.Select(attrs={
        "class": "form-control"}
      ))

    class Meta:
        model = EventList
        fields = ('eventname', 'evendate', 'predtime', 'emerge')


