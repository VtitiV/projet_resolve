from django.urls import path
from user_app.views import user_views

urlpatterns = [
    path('',user_views, name="user_views"),
]
