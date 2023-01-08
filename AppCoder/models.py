from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    anio = models.IntegerField()
    duracion = models.IntegerField()
    pais = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="posters")

    def __str__(self):
        return f"{self.nombre} ({self.anio}) - Director: {self.director}"

class director(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=80)
    foto = models.ImageField(upload_to="fotos", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Nacionalidad: {self.nacionalidad}"

class actor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=80)
    foto = models.ImageField(upload_to="fotos", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Nacionalidad: {self.nacionalidad}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatars")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"