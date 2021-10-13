# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import EventList, Dailyfreetime

# Register your models here.

class EventListAdmin(admin.ModelAdmin):
  list_display = ('username', 'eventname', 'eventdate', 'predtime', 'emerge', 'iscomplete', 'costtime')

  fields = ['username', 'eventname', 'eventdate', 'predtime', 'emerge', 'iscomplete', 'costtime']

class DailyfreetimeAdmin(admin.ModelAdmin):
  list_display = ('username', 'timedate', 'freetime')

  fields = ['username', 'timedate', 'freetime']

admin.site.register(EventList, EventListAdmin)
admin.site.register(Dailyfreetime, DailyfreetimeAdmin)