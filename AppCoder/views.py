from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from AppCoder.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DeleteView, ListView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.utils.timezone import datetime
from django.db.models import Avg

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

def index(request):
    return render(request, "AppCoder/index.html")

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

def busquedaPeli(request):
    return render (request, "AppCoder/busquedaPeli.html")

def buscarPeli(request):
    nombre = request.GET["nombre"]
    pelis = pelicula.objects.filter(nombre__contains=nombre)
    if nombre == "":
        return render (request, "AppCoder/busquedaPeli.html", {"mensaje": "Ingrese por favor una película"})
    if pelis:
        return render (request, "AppCoder/listarPelis.html", {"pelis": pelis})
    else:
        return render (request, "AppCoder/busquedaPeli.html", {"mensaje": "No se encontró ninguna película con ese nombre"})


def busquedaDirector(request):
    return render (request, "AppCoder/busquedaDirector.html")


def buscarDirector(request):
    nombre = request.GET["nombre"]
    directores = director.objects.filter(nombre__contains=nombre)
    if nombre == "": 
        return render (request, "AppCoder/busquedaDirector.html", {"mensaje": "Ingrese por favor un nombre"})
    if directores:
        return render (request, "AppCoder/listarDirectores.html", {"directores": directores})
    else:
        return render (request, "AppCoder/busquedaDirector.html", {"mensaje": "No se encontró ningún director con ese nombre"})
    

def busquedaActor(request):
    return render (request, "AppCoder/busquedaActor.html")

def buscarActor(request):
    nombre = request.GET["nombre"]
    actores = actor.objects.filter(nombre__contains=nombre)
    if nombre == "":
        return render (request, "AppCoder/busquedaActor.html", {"mensaje": "Ingrese por favor un nombre"})
    if actores:
        return render (request, "AppCoder/listarActores.html", {"actores": actores})
    else:
        return render (request, "AppCoder/busquedaActor.html", {"mensaje": "No se encontró ningún actor con ese nombre"})


def listarPelis(request):
    pelis = pelicula.objects.all()
    return render (request, "AppCoder/listarPelis.html", {"pelis": pelis})

@login_required
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


def listarDirectores(request):
    directores = director.objects.all()
    return render (request, "AppCoder/listarDirectores.html", {"directores": directores})

class borrarDirector(DeleteView, LoginRequiredMixin):
    model = director
    success_url = reverse_lazy("listarDirectores")

@login_required
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


def listarActores(request):
    actores = actor.objects.all()
    return render (request, "AppCoder/listarActores.html", {"actores": actores})

@login_required
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
    reviews = review.objects.filter(pelicula=peli)

    promedio = reviews.aggregate(Avg("puntaje"))["puntaje__avg"]
    if promedio is None:
        promedio = 0
    promedio = round(promedio, 2)
    
    context = {
        "pelicula": peli,
        "reviews": reviews,
        "promedio": promedio
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

@login_required
def agregarReview(request, id):
    peli = pelicula.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            review.objects.create(
                pelicula=peli,
                usuario=request.user,
                resenia=datos.get('resenia'),
                puntaje=datos.get('puntaje')
            )
            return redirect('detallePeli', id=peli.id)
    else:
        form = ReviewForm()
    return render(request, 'AppCoder/agregarReview.html', {'form': form})

@login_required
def editarReview(request, id):
    reviewcita = review.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=reviewcita)
        if form.is_valid():
            if reviewcita.puntaje > 10 or reviewcita.puntaje < 0:
                return render(request, 'AppCoder/editarReview.html', {'form': form, 'error': 'El puntaje debe estar entre 0 y 10'})
            form.save()
            return redirect('detallePeli', id=reviewcita.pelicula.id)
    else:
        form = ReviewForm(instance=reviewcita)
    return render(request, 'AppCoder/editarReview.html', {'form': form})

class borrarReview(DeleteView, LoginRequiredMixin):
    model = review
    success_url = reverse_lazy("listarPelis")

def sobremi(request):
    return render(request, "AppCoder/sobremi.html", {'imagen': "sobremi.jpg"})