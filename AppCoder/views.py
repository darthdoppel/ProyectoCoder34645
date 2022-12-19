from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def peliculas(request):
    return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/peliculas.html")

def directores(request):
    return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/directores.html")

def actores(request):
    return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/actores.html")

def inicio(request):
    return render (request, "C:/Users/leand/Desktop/Python/Entorno/virtual/ProyectoCoder/AppCoder/templates/AppCoder/inicio.html")