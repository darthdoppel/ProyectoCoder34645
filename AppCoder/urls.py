from django.urls import path
from .views import *

urlpatterns = [
    path("peliculas/", peliculas, name="peliculas"),
    path("directores/", directores, name="directores"),
    path("actores/", actores, name="actores"),
    path("", inicio, name="inicio"),
]