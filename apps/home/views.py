# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import NewEventForm
from django.shortcuts import render
from .models import EventList
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url="/login/")
def index(request):
    print('index')

    form = NewEventForm()

    return render(request, "home/index.html", {"form": form})


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
    form = NewEventForm(request.POST)
    print(form)

    username = request.user
    eventname = form.cleaned_data.get("eventname")
    eventdate = form.cleaned_data.get("eventdate")
    predtime = form.cleaned_data.get("predtime")
    emerge = form.cleaned_data.get("emerge")

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

    return render("home/index.html", {"form": form})
    # return HttpResponse("success")