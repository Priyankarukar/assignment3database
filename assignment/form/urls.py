from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.form,name='form'),
    path('check',views.getdata,name='getdata'),
]