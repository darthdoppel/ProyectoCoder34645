from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path("registro/", registro, name="registro"),
    path("ingreso/", ingreso, name="ingreso"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("EditarPerfil/", EditarPerfil, name="EditarPerfil"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    path("verperfil/", verperfil, name="verperfil"),
]   