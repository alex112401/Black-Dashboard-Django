# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class eventList(models.Model):
    userName = models.ForeignKey(User, on_delete = models.CASCADE)
    eventName = models.CharField(max_length=50)
    eventDate = models.DateField(null=True)
    predTime = models.FloatField(max_length=50)
    emerge = models.CharField(max_length=50)
    isComplete = models.BooleanField(default=False)
    costTime = models.FloatField(null=True, blank=True)

    # @classmethod
    # def create(cls, username, eventname, eventdate, predtime, emerge):
    #     event = cls(username=username, eventname=eventname, eventdate=eventdate, predtime=predtime, emerge=emerge)
    #     # do something with the book
    #     return event

    def __str__(self):
        """String for representing the Model object."""
        return self.eventName


class dailyFreeTime(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    timeDate = models.DateField(null=True)
    freeTime = models.FloatField(max_length=50)