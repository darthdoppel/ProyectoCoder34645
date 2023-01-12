from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class MensajeForm(forms.ModelForm):
    receptor = forms.ModelChoiceField(queryset=User.objects.all(), label='Para', required=True)
    cuerpo = forms.CharField(label='Mensaje', max_length=1000, required=True)

    class Meta:
        model = Mensaje
        fields = ('receptor', 'cuerpo')