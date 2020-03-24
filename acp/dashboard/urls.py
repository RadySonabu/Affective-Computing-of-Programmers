from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("next/", views.home, name="home"),
    path("about/", views.about, name="about"),
]
