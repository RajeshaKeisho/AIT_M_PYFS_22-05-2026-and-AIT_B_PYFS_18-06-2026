from django.urls import path 
from . import views

urlpatterns = [
    path("morning/", views.morning_message, name='morning'),
    path("noon/", views.noon_message, name='noon'),
    path("evening/", views.evening_message, name='evening'),
]
