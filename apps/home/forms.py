# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from datetime import date


class NewEventForm(forms.Form):
    today = date.today()

    eventname = forms.CharField(        
      widget=forms.TextInput(
        attrs={
          "placeholder": "EX: 會議 專案...",
          "class": "form-control",
          "list": "datalistOptions" ,
          "id": "eventname",
        }
      ))
      
    eventdate = forms.DateField(      
      widget=forms.TextInput(
        attrs={
          "class": "form-control",
          "type": "date",
          "id": "eventdate",
          "value": today
        }
      ))

    predtime = forms.FloatField(
      widget=forms.TextInput(
        attrs={
          "class": "form-control",
          "type": "number",
          "id": "predtime",
          "value":1, 
          "step": "0.1", 
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
        "class": "form-control",
        "id": "emerge"}
      ))

      
class NewDailyTimeForm(forms.Form):
    today = date.today()


    timedate = forms.DateField(      
      widget=forms.TextInput(
        attrs={
          "class": "form-control",
          "type": "date",
          "id": "timedate",
          "value": today
        }
      ))
    
    freetime = forms.FloatField(
      widget=forms.TextInput(
        attrs={
          "class": "form-control",
          "type": "number",
          "id": "freetime",
          "value":1, 
          "step": "0.1", 
          "min":"0"
        }
      ))
