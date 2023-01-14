from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class PeliForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", max_length=200)
    anio = forms.IntegerField(label="Año de estreno")
    duracion = forms.IntegerField(label="Duración (en minutos)")
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    pais = forms.CharField(label="País de origen", max_length=200)
    director = forms.ModelMultipleChoiceField(queryset=director.objects.all().order_by('nombre'), label="Director de la película", required=False, widget=forms.CheckboxSelectMultiple)
    poster = forms.URLField(label="Link del póster de la película", required=False)
    puntajepromedio = forms.FloatField(label="Puntaje promedio", initial=0)
    cast = forms.ModelMultipleChoiceField(queryset=actor.objects.all().order_by('nombre'), label="Actores", required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model= pelicula
        fields= ["nombre", "anio", "duracion", "descripcion", "pais", "director", "poster", "puntajepromedio", "cast"]
        help_texts= {k : "" for k in fields}

class ActorForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", max_length=80)
    apellido = forms.CharField(label="Apellido", max_length=80)
    edad = forms.IntegerField(label="Edad")
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=80)
    foto = forms.URLField(label="Foto del actor", required=False)
    peliculashechas = forms.ModelMultipleChoiceField(queryset=pelicula.objects.all().order_by('nombre'), label="Películas", required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model= actor
        fields= ["nombre", "apellido", "edad", "nacionalidad", "foto", "peliculashechas"]
        help_texts= {k : "" for k in fields}

class DirectorForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", max_length=80)
    apellido = forms.CharField(label="Apellido", max_length=80)
    edad = forms.IntegerField(label="Edad")
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=80)
    foto = forms.URLField(label="Foto del director", required=False)
    peliculashechas = forms.ModelMultipleChoiceField(queryset=pelicula.objects.all().order_by('nombre'), label="Películas", required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model= director
        fields= ["nombre", "apellido", "edad", "nacionalidad", "foto", "peliculashechas"]
        help_texts= {k : "" for k in fields}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = ["resenia", "puntaje"]
