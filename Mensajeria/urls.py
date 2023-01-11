from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path("mensajes/", mensajes, name="mensajes"),
]   