# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import NewEventForm, NewDailyTimeForm
from django.shortcuts import render, redirect
from .models import EventList, Dailyfreetime
from django.views.decorators.csrf import csrf_exempt



@login_required(login_url="/login/")
def index(request):
    print('index')

    eventForm = NewEventForm()
    timeForm = NewDailyTimeForm()

    return render(request, "home/index.html", {"eventForm": eventForm,
                                                "timeForm": timeForm})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required
@csrf_exempt
def newevent(request):
    print('newevent')
    print(request.method)

    if(request.method == "POST"):
      eventForm = NewEventForm(request.POST)
      if eventForm.is_valid():
        username = request.user
        eventname = eventForm.cleaned_data.get("eventname")
        eventdate = eventForm.cleaned_data.get("eventdate")
        predtime = eventForm.cleaned_data.get("predtime")
        emerge = eventForm.cleaned_data.get("emerge")

        print("username ",username)
        print("eventname ",eventname)
        print("eventdate ",eventdate)
        print("predtime ",predtime)
        print("emerge ",emerge)


        newevent = EventList.objects.create(
          username = username,
          eventname = eventname,
          eventdate = eventdate,
          predtime = predtime,
          emerge = emerge,
          iscomplete = False,
          costtime = None
        )

        newevent.save()
        
      else:
        eventForm = NewEventForm()
        print(eventForm.errors)
        print("eventForm is error")
    else:
      print("Not Post")
      eventForm = NewEventForm()

    print("back")
    return redirect('/')

@login_required
@csrf_exempt
def newfreetime(request):
    print('newfreetime')
    print(request.method)

    if(request.method == "POST"):
      timeForm = NewDailyTimeForm(request.POST)
      if timeForm.is_valid():
        username = request.user
        timedate = timeForm.cleaned_data.get("timedate")
        freetime = timeForm.cleaned_data.get("freetime")


        print("username ",username)
        print("timedate ",timedate)
        print("freetime ",freetime)



        newfreetime = Dailyfreetime.objects.create(
          username = username,
          timedate = timedate,
          freetime = freetime,
        )

        newfreetime.save()
        
      else:
        timeForm = NewDailyTimeForm()
        print(timeForm.errors)
        print("timeForm is error")
    else:
      print("Not Post")
      timeForm = NewDailyTimeForm()

    print("back")
    return redirect('/')