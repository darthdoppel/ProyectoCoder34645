from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from AppCoder.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.utils.timezone import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

def peliculas(request):
    return render (request, "AppCoder/listarPelis.html")

def directores(request):
    return render (request, "AppCoder/directores.html")

def actores(request):
    return render (request, "AppCoder/actores.html")

def index(request):
    return render (request, "AppCoder/index.html")
    

#Forms para cargar

@login_required
def peliFormulario(request):
    if request.method == "POST":
        form = PeliForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            nombre = detalles["nombre"]
            anio = detalles["anio"]
            duracion = detalles["duracion"]
            descripcion = detalles["descripcion"]
            pais = detalles["pais"]
            director = detalles["director"]
            poster = detalles["poster"]
            puntajepromedio = detalles["puntajepromedio"]

            nuevaPeli = pelicula(nombre=nombre, anio=anio, duracion=duracion, descripcion=descripcion, pais=pais, director=director, poster=poster, puntajepromedio=puntajepromedio)
            nuevaPeli.save()
            return render(request, "AppCoder/listarPelis.html", {"mensaje": "Película guardada con éxito"})

        else:
            return render(request, "AppCoder/peliFormulario.html", {"form": form, "mensaje": "Error al guardar la película"})
    else:
        formulario = PeliForm()
        return render(request, "AppCoder/peliFormulario.html", {"form": formulario, "controller": "Agregar película"})

@login_required
def actorForm(request):
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            nombre = detalles["nombre"]
            apellido = detalles["apellido"]
            edad = detalles["edad"]
            nacionalidad = detalles["nacionalidad"]
            foto = detalles["foto"]

            nuevoActor = actor(nombre=nombre, apellido=apellido, edad=edad, nacionalidad=nacionalidad, foto = foto)
            nuevoActor.save()
            return render(request, "AppCoder/listarActores.html", {"mensaje": "Actor guardado con éxito"})

        else:
            return render(request, "AppCoder/actorForm.html", {"form": formulario, "mensaje": "Error al guardar el actor"})

    else:
        formulario = ActorForm()
        return render(request, "AppCoder/actorForm.html", {"form": formulario})

@login_required
def directorForm(request):
    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            nombre = detalles["nombre"]
            apellido = detalles["apellido"]
            edad = detalles["edad"]
            nacionalidad = detalles["nacionalidad"]
            foto = detalles["foto"]

            nuevoDirector = director(nombre=nombre, apellido=apellido, edad=edad, nacionalidad=nacionalidad, foto = foto)
            nuevoDirector.save()
            return render(request, "AppCoder/listarDirectores.html", {"mensaje": "Director guardado con éxito"})

        else:
            return render(request, "AppCoder/directorForm.html", {"form": formulario, "mensaje": "Error al guardar el director"})

    else:
        formulario = DirectorForm()
        return render(request, "AppCoder/directorForm.html", {"form": formulario})

# Funciones y clases de pelis

def busquedaPeli(request):
    return render (request, "AppCoder/busquedaPeli.html")

def buscarPeli(request):
    nombre = request.GET["nombre"]
    if nombre != "":
        pelis = pelicula.objects.filter(nombre__icontains=nombre)
        return render (request, "AppCoder/resBusqPelis.html", {"pelis": pelis})
    else:
        return render (request, "AppCoder/busquedaPeli.html", {"mensaje": "No se encontró la película"})

def listarPelis(request):
    pelis = pelicula.objects.all()
    return render (request, "AppCoder/listarPelis.html", {"pelis": pelis})

@login_required
def editarPeli(request, id):
    peli = pelicula.objects.get(id=id)
    if request.method == "POST":
        form = PeliForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            peli.nombre = detalles["nombre"]
            peli.anio = detalles["anio"]
            peli.duracion = detalles["duracion"]
            peli.descripcion = detalles["descripcion"]
            peli.pais = detalles["pais"]
            peli.director = detalles["director"]
            peli.poster = detalles["poster"]
            peli.puntajepromedio = detalles["puntajepromedio"]
            peli.save()
            pelis = pelicula.objects.all()
            return render(request, "AppCoder/listarPelis.html", {"pelis": pelis, "mensaje": "Película editada con éxito"})
        pass
    else:
        formulario = PeliForm(initial={"nombre": peli.nombre, "anio": peli.anio, "duracion": peli.duracion, "descripcion": peli.descripcion, "pais": peli.pais, "director": peli.director, "poster": peli.poster, "puntajepromedio": peli.puntajepromedio})
        return render(request, "AppCoder/editarPeli.html", {"form": formulario, "peli": peli, "controller": "EDITAR PELICULA"})

class borrarPeli(DeleteView, LoginRequiredMixin):
    model = pelicula
    success_url = reverse_lazy("listarPelis")

# Funciones y clases de directores

def busquedaDirector(request):
    return render (request, "AppCoder/busquedaDirector.html")

def buscarDirector(request):
    nombre = request.GET["nombre"]
    if nombre !="":
        directores = director.objects.filter(nombre__icontains=nombre)
        return render (request, "AppCoder/resBusqDirectores.html", {"directores": directores})
    else:
        return render (request, "AppCoder/busquedaDirector.html", {"mensaje": "No se encontró al director"})

def listarDirectores(request):
    directores = director.objects.all()
    return render (request, "AppCoder/listarDirectores.html", {"directores": directores})

@login_required
def editarDirector(request, id):
    directors = director.objects.get(id=id)
    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            directors.nombre = detalles["nombre"]
            directors.apellido = detalles["apellido"]
            directors.edad = detalles["edad"]
            directors.nacionalidad = detalles["nacionalidad"]
            directors.foto = detalles["foto"]
            directors.save()
            directores = director.objects.all()
            return render(request, "AppCoder/listarDirectores.html", {"directores": directores, "mensaje": "Director editado con éxito"})
        pass
    else:
        formulario = DirectorForm(initial = {"nombre": directors.nombre, "apellido": directors.apellido, "edad": directors.edad, "nacionalidad": directors.nacionalidad, "foto": directors.foto})
        return render(request, "AppCoder/editarDirector.html", {"form": formulario, "director": directors})

class borrarDirector(DeleteView, LoginRequiredMixin):
    model = director
    success_url = reverse_lazy("listarDirectores")

# Funciones y clases de actores

def busquedaActor(request):
    return render (request, "AppCoder/busquedaActor.html")

def buscarActor(request):
    nombre = request.GET["nombre"]
    if nombre !="":
        actores = actor.objects.filter(nombre__icontains=nombre)
        return render (request, "AppCoder/resBusqActores.html", {"actores": actores})
    else:
        return render (request, "AppCoder/busquedaActor.html", {"mensaje": "No se encontró al actor"})

def listarActores(request):
    actores = actor.objects.all()
    return render (request, "AppCoder/listarActores.html", {"actores": actores})

@login_required
def editarActor(request, id):
    actors = actor.objects.get(id=id)
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            detalles = form.cleaned_data
            actors.nombre = detalles["nombre"]
            actors.apellido = detalles["apellido"]
            actors.edad = detalles["edad"]
            actors.nacionalidad = detalles["nacionalidad"]
            actors.foto = detalles["foto"]
            actors.save()
            actores = actor.objects.all()
            return render(request, "AppCoder/listarActores.html", {"actores": actores, "mensaje": "Actor editado con éxito"})
        pass
    else:
        formulario = ActorForm(initial = {"nombre": actors.nombre, "apellido": actors.apellido, "edad": actors.edad, "nacionalidad": actors.nacionalidad, "foto": actors.foto})
        return render(request, "AppCoder/editarActor.html", {"form": formulario, "actor": actors, "controller": "EDITAR ACTOR"})

class borrarActor(DeleteView, LoginRequiredMixin):
    model = actor
    success_url = reverse_lazy("listarActores")

def detallePeli(request, id):
    peli = pelicula.objects.get(id=id)
    
    context = {
        "pelicula": peli
    }
    return render(request, "AppCoder/detallePeli.html", context)

def detalleActor(request, id):
    actorcito = actor.objects.get(id=id)
    
    context = {
        "actor": actorcito
    }
    return render(request, "AppCoder/detalleActor.html", context)

def detalleDirector(request, id):
    directorcito = director.objects.get(id=id)
    
    context = {
        "director": directorcito
    }
    return render(request, "AppCoder/detalleDirector.html", context)