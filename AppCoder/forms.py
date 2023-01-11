from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class PeliForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=200)
    anio = forms.IntegerField(label="Año de estreno")
    duracion = forms.IntegerField(label="Duración (en minutos)")
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    pais = forms.CharField(label="País de origen", max_length=200)
    director = forms.CharField(label="Director de la película", max_length=200)
    poster = forms.URLField(label="Link del póster de la película", required=False)
    puntajepromedio = forms.FloatField(label="Puntaje promedio", initial=0)
    peliculashechas = forms.ModelMultipleChoiceField(queryset=actor.objects.all(), label="Actores", required=False)

    class Meta:
        model= User
        fields= ["nombre", "anio", "duracion", "pais", "director", "poster"]
        help_texts= {k : "" for k in fields}

class ActorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=80)
    apellido = forms.CharField(label="Apellido", max_length=80)
    edad = forms.IntegerField(label="Edad")
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=80)
    foto = forms.URLField(label="Foto del actor", required=False)

class DirectorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=80)
    apellido = forms.CharField(label="Apellido", max_length=80)
    edad = forms.IntegerField(label="Edad")
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=80)
    foto = forms.URLField(label="Foto del director", required=False)