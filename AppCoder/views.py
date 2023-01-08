from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppCoder.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages as message

def agregarpeliculas(request):
    return render (request, "AppCoder/agregarpeliculas.html")

def directores(request):
    return render (request, "AppCoder/directores.html")

def actores(request):
    return render (request, "AppCoder/actores.html")

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            nombreusuario = form.cleaned_data.get('username')
            message.success(request, f'Usuario {nombreusuario} creado con éxito')
        else:
            for msg in form.error_messages:
                message.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        form = UserCreationForm()
    return render (request, "AppCoder/registro.html")

def peliFormulario(request):
    if request.method == "POST":
        form = PeliForm(request.POST)
        if form.is_valid():
            detalles = form.cleaned_data
            nombre = detalles["nombre"]
            anio = detalles["anio"]
            duracion = detalles["duracion"]
            pais = detalles["pais"]
            director = detalles["director"]

            nuevaPeli = pelicula(nombre=nombre, anio=anio, duracion=duracion, pais=pais, director=director)
            nuevaPeli.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Película guardada con éxito"})

        else:
            return render(request, "AppCoder/peliFormulario.html", {"form": formulario, "mensaje": "Error al guardar la película"})
    else:
        formulario = PeliForm()
        return render(request, "AppCoder/peliFormulario.html", {"form": formulario})

def actorForm(request):
    if request.method == "POST":
        form = ActorForm(request.POST)
        if form.is_valid():
            detalles = form.cleaned_data
            nombre = detalles["nombre"]
            apellido = detalles["apellido"]
            edad = detalles["edad"]
            nacionalidad = detalles["nacionalidad"]

            nuevoActor = actor(nombre=nombre, apellido=apellido, edad=edad, nacionalidad=nacionalidad)
            nuevoActor.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Actor guardado con éxito"})

        else:
            return render(request, "AppCoder/actorForm.html", {"form": formulario, "mensaje": "Error al guardar el actor"})

    else:
        formulario = ActorForm()
        return render(request, "AppCoder/actorForm.html", {"form": formulario})

def directorForm(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            detalles = form.cleaned_data
            nombre = detalles["nombre"]
            apellido = detalles["apellido"]
            edad = detalles["edad"]
            nacionalidad = detalles["nacionalidad"]

            nuevoDirector = director(nombre=nombre, apellido=apellido, edad=edad, nacionalidad=nacionalidad)
            nuevoDirector.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Director guardado con éxito"})

        else:
            return render(request, "AppCoder/directorForm.html", {"form": formulario, "mensaje": "Error al guardar el director"})

    else:
        formulario = DirectorForm()
        return render(request, "AppCoder/directorForm.html", {"form": formulario})

def busquedaPeli(request):
    return render (request, "AppCoder/busquedaPeli.html")

def buscar(request):
    nombre = request.GET["nombre"]
    if nombre !="":
        pelis = pelicula.objects.filter(nombre__icontains=nombre)
        return render (request, "AppCoder/resBusqPelis.html", {"pelis": pelis})
    else:
        return render (request, "AppCoder/busquedaPeli.html", {"mensaje": "No se encontró la película"})


def listarPelis(request):
    pelis = pelicula.objects.all()
    return render (request, "AppCoder/listarPelis.html", {"pelis": pelis})

def editarPeli(request, id):
    peli = pelicula.objects.get(id=id)
    if request.method == "POST":
        form = PeliForm(request.POST)
        if form.is_valid():
            detalles = form.cleaned_data
            peli.nombre = detalles["nombre"]
            peli.anio = detalles["anio"]
            peli.duracion = detalles["duracion"]
            peli.pais = detalles["pais"]
            peli.director = detalles["director"]
            peli.save()
            pelis = pelicula.objects.all()
            return render(request, "AppCoder/listarPelis.html", {"pelis": pelis, "mensaje": "Película editada con éxito"})
        pass
    else:
        formulario = PeliForm(initial = {"nombre": peli.nombre, "anio": peli.anio, "duracion": peli.duracion, "pais": peli.pais, "director": peli.director})
        return render(request, "AppCoder/editarPeli.html", {"form": formulario, "peli": peli})

def eliminarPeli (request, id):
    peli = pelicula.objects.get(id=id)
    peli.delete()
    pelis = pelicula.objects.all()
    return render(request, "AppCoder/listarPelis.html", {"pelis": pelis, "mensaje": "Película eliminada con éxito"})