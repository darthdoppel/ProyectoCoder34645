from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from Usuarios.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

# Vista de registro

def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
           username = form.cleaned_data["username"]
           form.save()
           return render(request, "AppCoder/index.html", {"mensaje": f"Registro del usuario {username} exitoso"})
        else:
            return render(request, "registroForm.html", {"form": form})
    else:
        form = RegistroUsuarioForm()
        return render(request, "registroForm.html", {"form": form})

# Vista de login

def ingreso(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            user=datos["username"]
            contrasenia=datos["password"]
            usuario = authenticate(username=user, password=contrasenia)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/index.html", {"mensaje": f"Ingreso del usuario {user} exitoso"})
            else:
                return render(request, "loginForm.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "loginForm.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
    else:
        form = AuthenticationForm()
        return render(request, "loginForm.html", {"form": form})
    
        


# Editar perfiles

@login_required
def EditarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = EditarPerfilForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            usuario.email = datos["email"]
            usuario.password1 = datos["password1"]
            usuario.password2 = datos["password2"]
            usuario.first_name = datos["first_name"]
            usuario.last_name = datos["last_name"]
            usuario.save()
            return render(request, "AppCoder/index.html", {"mensaje": "Perfil editado con éxito"})
        else:
            return render(request, "editarPerfil.html", {"form": form})
    else:
        form = EditarPerfilForm(instance=usuario)
        return render(request, "editarPerfil.html", {"form": form, "nombreusuario": usuario.username})

@login_required
def mostrarAvatar(request):
    lista = Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
            avatar = lista[0].imagen.url
    else:
            avatar = "media/avatars/default.png"
    return avatar

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        formu = AvatarForm(request.POST, request.FILES)
        if formu.is_valid():
            avatar = Avatar(user=request.user, imagen=request.FILES['imagen'])
            avatarAnterior = Avatar.objects.filter(user=request.user)
            if len(avatarAnterior)>0:
                avatarAnterior.delete()
            avatar.save()
            return render (request, "AppCoder/index.html", {"mensaje": "Avatar guardado con éxito"})
        else:
            return render(request, "agregarAvatar.html", {"form": formu, "usuario": request.user, "mensaje": "Error al guardar el avatar"})
    else:
        form = AvatarForm()
        return render(request, "agregarAvatar.html", {"form": form, "usuario": request.user})