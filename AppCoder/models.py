from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    anio = models.IntegerField()
    duracion = models.IntegerField()
    descripcion = models.TextField(null = True, blank = True)
    pais = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    poster = models.URLField(default=None, null=True, blank=True)
    puntajepromedio = models.FloatField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.anio}) - Director: {self.director}"

class director(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=80)
    foto = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Nacionalidad: {self.nacionalidad}"

class actor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=80)
    foto = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Nacionalidad: {self.nacionalidad}"