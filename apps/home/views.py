# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import newEventForm
from .models import eventList




@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


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
        
@login_required(login_url="/login/")
def newevent(request):

  form = newEventForm
  print('get form')
  userName = request.seession.get('userName')
  eventName = form.cleaned_data.get("eventName")
  eventDate = form.cleaned_data.get("eventDate")
  predTime = form.cleaned_data.get("predTime")
  emerge = form.cleaned_data.get("emerge")

  newEvent = eventList.object.create(
    userName = userName,
    eventName = eventName,
    eventDate = eventDate,
    predTime = predTime,
    emerge = emerge
  )

  newEvent.save()

  return HttpResponse("success")