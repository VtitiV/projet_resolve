from django.urls import path
from .views import demandedepart

urlpatterns = [
    path('',demandedepart, name="demandedepart"),

]