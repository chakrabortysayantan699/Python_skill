from django.contrib import admin
from django.urls import path,include 
from . import views 
app_name='adminapp'

urlpatterns=[
    
    path('test', views.index, name='index'),
    path('', views.test, name='test'),
]