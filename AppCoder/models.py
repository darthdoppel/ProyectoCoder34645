from django.db import models

# Create your models here.


class pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    anio = models.IntegerField()
    duracion = models.IntegerField()
    pais = models.CharField(max_length=200)
    director = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} ({self.anio}) - Director: {self.director}"

class director(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Nacionalidad: {self.nacionalidad}"

class actor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Nacionalidad: {self.nacionalidad}"

class Usuario(models.Model):
    nombreusuario = models.CharField(max_length=80)
    email = models.EmailField()
    