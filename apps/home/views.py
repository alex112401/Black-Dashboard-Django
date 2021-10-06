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



@login_required(login_url="/login/")
def index(request):
    # context = {'segment': 'index'}

    # html_template = loader.get_template('home/index.html')
    # return HttpResponse(html_template.render(context, request))
    if request.method == "POST":
        form = NewEventForm(request.POST)
        if form.is_valid():
            form.save()
            eventname = form.cleaned_data.get("eventname")

            # return redirect("/login/")

    else:
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

# def NewEvent(request):

#     if request.method == "POST":
#         form = NewEventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             eventname = form.cleaned_data.get("eventname")

#             # return redirect("/login/")



#     return render(request, "home/index.html", {"form": form, "eventname": eventname})