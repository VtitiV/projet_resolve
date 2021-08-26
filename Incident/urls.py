from django.urls import path
from .views import incidentdepart

urlpatterns = [
    path('',incidentdepart, name="incidentdepart"),

]