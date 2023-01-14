from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    anio = models.IntegerField()
    duracion = models.IntegerField()
    descripcion = models.TextField(null = True, blank = True)
    pais = models.CharField(max_length=200)
    director = models.ManyToManyField('director', related_name="pelishechasdirector", blank=True)
    poster = models.URLField(default=None, null=True, blank=True)
    puntajepromedio = models.FloatField(default=0)
    cast = models.ManyToManyField('actor', related_name="pelishechasactores", blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.anio})"

class director(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=80)
    foto = models.URLField(null=True, blank=True)
    pelishechas = models.ManyToManyField(pelicula, related_name="pelishechasdirector", blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class actor(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=80)
    foto = models.URLField(null=True, blank=True)
    pelishechas = models.ManyToManyField(pelicula, related_name="pelishechasactores", blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class review(models.Model):
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE, related_name="reviews")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    resenia = models.TextField()
    puntaje = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.pelicula} - {self.usuario}"