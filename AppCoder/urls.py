from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('', index, name="index"),
    path("peliFormulario/", peliFormulario, name="peliFormulario"),
    path("actorForm/", actorForm, name="actorForm"),
    path("directorForm/", directorForm, name="directorForm"),
    path("busquedaPeli/", busquedaPeli, name="busquedaPeli"),
    path("buscarPeli/", buscarPeli, name="buscarPeli"),
    path("listarPelis/", listarPelis, name="listarPelis"),
    path("editarPeli/<id>", editarPeli, name="editarPeli"),
    path('pelicula/borrar/<pk>', borrarPeli.as_view(), name='borrarPeli'),
    path("listarDirectores/", listarDirectores, name="listarDirectores"),
    path("editarDirector/<id>", editarDirector, name="editarDirector"),
    path('director/borrar/<pk>', borrarDirector.as_view(), name='borrarDirector'),
    path("busquedaDirector/", busquedaDirector, name="busquedaDirector"),
    path('buscarDirector/', buscarDirector, name='buscarDirector'),
    path("busquedaActor", busquedaActor, name="busquedaActor"),
    path("listarActores/", listarActores, name="listarActores"),
    path("editarActor/<id>", editarActor, name="editarActor"),
    path("buscarActor/", buscarActor, name="buscarActor"),
    path("actor/borrar/<pk>)", borrarActor.as_view(), name="borrarActor"),
    path("detallePeli/<int:id>/", detallePeli, name="detallePeli"),
    path("detalleActor/<int:id>/", detalleActor, name="detalleActor"),
    path("detalleDirector/<int:id>/", detalleDirector, name="detalleDirector"),
    path("agregarReview/<id>/", agregarReview, name="agregarReview"),
    path("editarReview/<id>/", editarReview, name="editarReview"),
    path("borrarReview/<pk>/", borrarReview.as_view(), name="borrarReview"),
]   