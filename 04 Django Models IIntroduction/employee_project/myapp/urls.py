from django.urls import path
from .views import employeelist

urlpatterns = [
    path("emplist/", employeelist, name='emplist'),
]
