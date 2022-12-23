from django import forms

class PeliForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=200)
    anio = forms.IntegerField(label="Año de estreno")
    duracion = forms.IntegerField(label="Duración (en minutos)")
    pais = forms.CharField(label="País de origen", max_length=200)
    director = forms.CharField(label="Director de la película", max_length=200)

class ActorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=80)
    apellido = forms.CharField(label="Apellido", max_length=80)
    edad = forms.IntegerField(label="Edad")
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=80)

class DirectorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=80)
    apellido = forms.CharField(label="Apellido", max_length=80)
    edad = forms.IntegerField(label="Edad")
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=80)