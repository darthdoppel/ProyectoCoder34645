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

def mensajes(request):
    return render(request, 'mensajes.html')