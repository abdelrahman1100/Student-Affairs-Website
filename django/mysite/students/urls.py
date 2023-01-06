from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import authenticate, login
from . import views
urlpatterns = [
    path('Addrecord', views.Addrecord, name='Addrecord'),
    path('info', views.info, name="info"),
    path('graduated', views.graduated, name="graduated"),
    path('first', views.first, name="first"),
    path('dept', views.choosedep, name="dept"),
    path('project', views.chooseproject, name="project"),
    path('home', views.main, name="home"),
    path('add', views.add, name="add")
]
