from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, get_user_model

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.template import loader
from Usuarios.views import *
from Mensajeria.forms import MensajeForm

def enviarMensajes(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            receptor = User.objects.get(username=form.cleaned_data['receptor'])
            emisor = request.user
            cuerpo = form.cleaned_data['cuerpo']
            leido = False
            mensaje = Mensaje(receptor=receptor, emisor=emisor, cuerpo=cuerpo)
            mensaje.save()
            return redirect('mensajesEnviados')
    else:
        form = MensajeForm()
    return render(request, 'enviarMensajes.html', {'form': form})

def mensajesRecibidos(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha')
    return render(request, 'mensajesRecibidos.html', {'mensajes': mensajes})

def mensajesEnviados(request):
    mensajes = Mensaje.objects.filter(emisor=request.user).order_by('-fecha')
    return render(request, 'mensajesEnviados.html', {'mensajes': mensajes})

def leerMensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.leido = True
    mensaje.save()

    return render(request, 'leerMensaje.html', {'mensaje': mensaje})