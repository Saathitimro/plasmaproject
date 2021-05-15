
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('donor', views.doner),
    path('donor_submit', views.doner_submit),
    path('liveRequest', views.liveRequest, name="liveRequest"),
    path('requestDonor', views.requestDonor, name="requestDonor"),
]
