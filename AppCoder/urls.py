from django.urls import path
from .views import *

urlpatterns = [
    path("peliculas/", peliculas, name="peliculas"),
    path("directores/", directores, name="directores"),
    path("actores/", actores, name="actores"),
    path("", inicio, name="inicio"),
    path("peliFormulario/", peliFormulario, name="peliFormulario"),
    path("actorForm/", actorForm, name="actorForm"),
    path("directorForm/", directorForm, name="directorForm"),
    path("busquedaPeli/", busquedaPeli, name="busquedaPeli"),
    path("buscar/", buscar, name="buscar"),
]