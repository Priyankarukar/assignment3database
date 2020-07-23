from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('form',views.form,name='form'),
    path('index',views.index,name='index'),
    path('check',views.getdata,name='getdata'),
]