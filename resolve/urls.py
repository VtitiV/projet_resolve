
from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [
    path('incidents/',include('Incident.urls')),
    path('',index, name="index"),
    path('admin/', admin.site.urls),
]
