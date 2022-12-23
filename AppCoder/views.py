from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppCoder.forms import *

def peliculas(request):
    return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/peliculas.html")

def directores(request):
    return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/directores.html")

def actores(request):
    return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/actores.html")

def inicio(request):
    return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/inicio.html")

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
            return render(request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/inicio.html", {"mensaje": "Película guardada con éxito"})

        else:
            return render(request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/peliFormulario.html", {"form": formulario, "mensaje": "Error al guardar la película"})
    else:
        formulario = PeliForm()
        return render(request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/peliFormulario.html", {"form": formulario})

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
            return render(request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/inicio.html", {"mensaje": "Actor guardado con éxito"})

        else:
            return render(request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/actorForm.html", {"form": formulario, "mensaje": "Error al guardar el actor"})

    else:
        formulario = ActorForm()
        return render(request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/actorForm.html", {"form": formulario})

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
            return render(request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/inicio.html", {"mensaje": "Director guardado con éxito"})

        else:
            return render(request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/directorForm.html", {"form": formulario, "mensaje": "Error al guardar el director"})

    else:
        formulario = DirectorForm()
        return render(request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/directorForm.html", {"form": formulario})

def busquedaPeli(request):
    return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/busquedaPeli.html")

def buscar(request):
    nombre = request.GET["nombre"]
    if nombre !="":
        pelis = pelicula.objects.filter(nombre__icontains=nombre)
        return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/resBusqPelis.html", {"pelis": pelis})
    else:
        return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/busquedaPeli.html", {"mensaje": "No se encontró la película"})