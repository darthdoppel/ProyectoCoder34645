from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

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