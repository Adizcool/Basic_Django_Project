#This was created manually inside app and content copied from urls of project

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    #here, we import the index function from view and display that when this url is given
    #Url used will be localhost/centrain/central -> first path from project then from the app
    path('central/', views.get_sites),
    path('sites/', views.Site_list.as_view())
]