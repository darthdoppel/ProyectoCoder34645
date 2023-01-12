from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path("enviarMensajes/", enviarMensajes, name="enviarMensajes"),
    path("mensajesRecibidos/", mensajesRecibidos, name="mensajesRecibidos"),
    path("mensajesEnviados/", mensajesEnviados, name="mensajesEnviados"),
    path("leerMensaje/<int:id>/", leerMensaje, name="leerMensaje"),
]   