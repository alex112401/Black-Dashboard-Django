# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json
from django.core import serializers
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


    eventForm = NewEventForm()
    timeForm = NewDailyTimeForm()
    eventList = EventList.objects.filter(iscomplete = False, username = request.user).values("eventname", "eventdate", "predtime", "emerge")
    comeventList = EventList.objects.filter(iscomplete = True, username = request.user).values("eventname", "eventdate", "predtime", "costtime", "emerge")
    dailyfreetime = Dailyfreetime.objects.filter(username = request.user)
    # eventListJson =
    # eventListJson = EventSerilizer(eventList)
    # print(type(eventListJson))
    # print(eventListJson)
    # eventList = list(eventList)
    # eventListobj = json.loads(eventListJson)
    


    return render(request, "home/index.html", {"eventForm": eventForm,
                                                "timeForm": timeForm,
                                                "eventlist":eventList,
                                                "comeventlist":comeventList,
                                                "dailyfreetime":dailyfreetime})


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
    if request.method == "POST":
      eventForm = NewEventForm(request.POST)

      if eventForm.is_valid():
        username = request.user
        eventname = eventForm.cleaned_data.get("eventname")
        eventdate = eventForm.cleaned_data.get("eventdate")
        predtime = eventForm.cleaned_data.get("predtime")
        emerge = eventForm.cleaned_data.get("emerge")
        checkEvents = EventList.objects.filter(eventdate = eventdate, iscomplete = False)
        totaltime = 0

        if Dailyfreetime.objects.filter(timedate = eventdate).exists():
          timeofdate = Dailyfreetime.objects.get(timedate = eventdate).freetime

          for event in checkEvents:
            totaltime += event.predtime
            print("totaltime", totaltime)
            print("timeofdate", timeofdate)
          
          if totaltime + predtime <= timeofdate:
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
            
            busyday = Dailyfreetime.objects.get(timedate = eventdate)
            busyday.busytime = totaltime + predtime
            busyday.save()
          else:
            print("out of time")
        else:
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
    else:
      eventForm = NewEventForm()
    return redirect('/')


@login_required
@csrf_exempt
def newfreetime(request):

    if request.method == "POST":
      timeForm = NewDailyTimeForm(request.POST)
      if timeForm.is_valid():
        username = request.user
        timedate = timeForm.cleaned_data.get("timedate")
        freetime = timeForm.cleaned_data.get("freetime")

        if Dailyfreetime.objects.filter(timedate = timedate).exists():
          obj = Dailyfreetime.objects.get(timedate = timedate)
          obj.freetime = freetime
          obj.save()

        else:
          newfreetime = Dailyfreetime.objects.create(
            username = username,
            timedate = timedate,
            freetime = freetime,
            busytime = 0
          )
          newfreetime.save()
        
      else:
        timeForm = NewDailyTimeForm()
    else:
      timeForm = NewDailyTimeForm()
    return redirect('/')


@login_required
@csrf_exempt
def deleteevent(request, pk):

    delevent = EventList.objects.get(pk=pk)
    delevent.delete()

    timeobj = Dailyfreetime.objects.get(timedate = delevent.eventdate)
    timeobj.busytime -= int(delevent.predtime)
    timeobj.save()

    return redirect('/')


@login_required
@csrf_exempt
def completeevent(request, pk):
    comevent = EventList.objects.get(pk=pk)
    costtime = request.POST.get('costtime')

    if(costtime!=0):

      comevent.iscomplete = True
      comevent.costtime = int(costtime)
      comevent.save()

      timeobj = Dailyfreetime.objects.get(timedate = comevent.eventdate)
      timeobj.busytime -= int(comevent.predtime)
      timeobj.save()

    return redirect('/')