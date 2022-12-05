from django.shortcuts import render
from .models import persona
from django.http import HttpResponse

def Familiar(request):
    familiar= persona(nombre="Julieta", vinculo="Hija", edad=27, fechanac="1994-06-27")
    familiar2= persona(nombre="Luis", vinculo="Padre", edad=57, fechanac="1965-06-27")
    familiar3= persona(nombre="Maria", vinculo="Madre", edad=57, fechanac="1965-06-27")
    familiar.save()
    familiar2.save()
    familiar3.save()
    cadena_texto= f"Familiar 1 guardado: Nombre: {familiar.nombre}, Vinculo: {familiar.vinculo}, Edad: {familiar.edad}, Fecha de Nacimiento: {familiar.fechanac}"
    cadena_texto2=f"Familiar 2 guardado: Nombre: {familiar2.nombre}, Vinculo: {familiar2.vinculo}, Edad: {familiar2.edad}, Fecha de Nacimiento: {familiar2.fechanac}"
    cadena_texto3=f"Familiar 3 guardado: Nombre: {familiar3.nombre}, Vinculo: {familiar3.vinculo}, Edad: {familiar3.edad}, Fecha de Nacimiento: {familiar3.fechanac}"
    return HttpResponse(cadena_texto + "<br>" + cadena_texto2 + "<br>" + cadena_texto3)