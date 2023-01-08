from django.urls import path
from .views import *

urlpatterns = [
    path("agregarpeliculas/", agregarpeliculas, name="agregarpeliculas"),
    path("directores/", directores, name="directores"),
    path("actores/", actores, name="actores"),
    path("", inicio, name="inicio"),
    path("peliFormulario/", peliFormulario, name="peliFormulario"),
    path("actorForm/", actorForm, name="actorForm"),
    path("directorForm/", directorForm, name="directorForm"),
    path("busquedaPeli/", busquedaPeli, name="busquedaPeli"),
    path("buscar/", buscar, name="buscar"),
    path("registro/", registro, name="registro"),
    path("listarPelis/", listarPelis, name="listarPelis"),
    path("editarPeli/<id>", editarPeli, name="editarPeli"),
    path("eliminarPeli/<id>", eliminarPeli, name="eliminarPeli"),
]