from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def morning_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h2>Hello, Good Morning! Now the time is " + formatted_time + ".")

def noon_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h2>Hello, Good Noon! Now the time is " + formatted_time + ".")

def evening_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h2>Hello, Good Eveninng! Now the time is " + formatted_time + ".")

