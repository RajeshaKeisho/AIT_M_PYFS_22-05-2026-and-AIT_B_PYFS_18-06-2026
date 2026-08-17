from django.urls import path
from .views import job_application_view, contact_view

urlpatterns = [
    path('job_application', job_application_view, name="job_application"),
    path('contact', contact_view, name="contact"),
]
