from django import views
from django.contrib import admin
from django.urls import path

from tourapp import views

urlpatterns = [

     path('',views.demo,name='demo'),

]
