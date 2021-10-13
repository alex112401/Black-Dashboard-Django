# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('newevent/', views.newevent, name='newevent'),
    path('newfreetime/', views.newfreetime, name='newfreetime'),
    path('deleteevent/<int:pk>', views.deleteevent),
    path('completeevent/<int:pk>', views.completeevent),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages')


]
