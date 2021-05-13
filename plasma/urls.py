
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('donor', views.doner),
    path('donor_submit', views.doner_submit),
]
