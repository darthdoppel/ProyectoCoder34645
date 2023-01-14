from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from AppCoder.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DeleteView, ListView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.utils.timezone import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

def peliculas(request):
    return render (request, "AppCoder/listarPelis.html")

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
            poster = detalles["poster"]
            puntajepromedio = detalles["puntajepromedio"]
            nuevaPeli = pelicula(nombre=nombre, anio=anio, duracion=duracion, descripcion=descripcion, pais=pais, poster=poster, puntajepromedio=puntajepromedio)
            nuevaPeli.save()

            actores = actor.objects.filter(id__in=request.POST.getlist('actores'))
            nuevaPeli.actores.add(*actores)

            directores = director.objects.filter(id__in=request.POST.getlist('directores'))
            nuevaPeli.directores.add(*directores)

            return render(request, "AppCoder/listarPelis.html", {"mensaje": "Película guardada con éxito"})

        else:
            return render(request, "AppCoder/peliFormulario.html", {"form": formulario, "mensaje": "Error al guardar la película"})

    else:
        formulario = PeliForm()
        return render(request, "AppCoder/peliFormulario.html", {"form": formulario})


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

            pelishechas = pelicula.objects.filter(id__in=request.POST.getlist('peliculashechas'))
            nuevoActor.pelishechas.add(*pelishechas)

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
            

            
            pelishechas = pelicula.objects.filter(id__in=request.POST.getlist('peliculashechas'))
            nuevoDirector.pelishechas.add(*pelishechas)
            nuevoDirector.pelishechas.set(pelishechas)

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

def editarPeli(request, id):
    peli = pelicula.objects.get(id=id)
    datos = {
        'form': PeliForm(instance=peli)
    }
    if request.method == 'POST':
        formulario = PeliForm(data=request.POST, instance=peli)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Película modificada con éxito"
            datos['form'] = formulario

    return render(request, "AppCoder/editarPeli.html", datos)

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

class borrarDirector(DeleteView, LoginRequiredMixin):
    model = director
    success_url = reverse_lazy("listarDirectores")

def editarDirector(request, id):
    directorcitos = director.objects.get(id=id)
    datos = {
        'form': DirectorForm(instance=directorcitos, initial={'peliculashechas': directorcitos.pelishechas.all()})
    }
    if request.method == 'POST':
        formulario = DirectorForm(data=request.POST, instance=directorcitos)
        if formulario.is_valid():
            pelishechas = formulario.cleaned_data['peliculashechas']
            nuevoActor = formulario.save()
            nuevoActor.pelishechas.set(pelishechas)
            datos['mensaje'] = "Director modificado con éxito"
            datos['form'] = formulario

    return render(request, "AppCoder/editarDirector.html", datos)

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

def editarActor(request, id):
    actorcitos = actor.objects.get(id=id)
    datos = {
        'form': ActorForm(instance=actorcitos, initial={'peliculashechas': actorcitos.pelishechas.all()})
    }
    if request.method == 'POST':
        formulario = ActorForm(data=request.POST, instance=actorcitos)
        if formulario.is_valid():
            pelishechas = formulario.cleaned_data['peliculashechas']
            nuevoActor = formulario.save()
            nuevoActor.pelishechas.set(pelishechas)
            datos['mensaje'] = "Actor modificado con éxito"
            datos['form'] = formulario

    return render(request, "AppCoder/editarActor.html", datos)



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