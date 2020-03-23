from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    
    path('download/', views.download, name='download' ),
    path('download-excel/', views.export, name='download-excel'),
]
