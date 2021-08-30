from django.urls import path, include
from .views import demandedepart, demande_de_compte

urlpatterns = [
    path('',demandedepart, name="demandedepart"),
    path('demande_de_compte/',demande_de_compte, name="demande_de_compte"),

]