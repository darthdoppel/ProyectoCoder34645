from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

class PeliForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=200)
    anio = forms.IntegerField(label="Año de estreno")
    duracion = forms.IntegerField(label="Duración (en minutos)")
    pais = forms.CharField(label="País de origen", max_length=200)
    director = forms.CharField(label="Director de la película", max_length=200)
    poster = forms.ImageField(label="Poster de la película", required=False)

    class Meta:
        model= User
        fields= ["nombre", "anio", "duracion", "pais", "director", "poster"]
        help_texts= {k : "" for k in fields}

class ActorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=80)
    apellido = forms.CharField(label="Apellido", max_length=80)
    edad = forms.IntegerField(label="Edad")
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=80)
    foto = forms.ImageField(label="Foto del actor", required=False)

class DirectorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=80)
    apellido = forms.CharField(label="Apellido", max_length=80)
    edad = forms.IntegerField(label="Edad")
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=80)
    foto = forms.ImageField(label="Foto del director", required=False)

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Email usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", max_length=150)
    last_name = forms.CharField(label="Apellido", max_length=150)

    class Meta:
        model= User
        fields= ["username", "email", "password1", "password2"]
        help_texts= {k : "" for k in fields}

class EditarPerfilForm(UserCreationForm):
    email= forms.EmailField(label="Email usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre", max_length=150)
    last_name = forms.CharField(label="Apellido", max_length=150)

    class Meta:
        model= User
        fields= ["email", "password1", "password2", "first_name", "last_name"]
        help_texts= {k : "" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen de perfil")