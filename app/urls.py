from django.contrib import admin
from django.urls import path
from app import views
from .views import *
urlpatterns=[
    path('',views.home, name='home'),
    path('add',views.add, name='add')
]
