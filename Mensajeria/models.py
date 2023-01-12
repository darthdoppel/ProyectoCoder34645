from django.db import models
from django.contrib.auth.models import User
from Usuarios.models import Avatar
from datetime import datetime   

# Create your models here.

LEIDO = (
    (True, 'Leido'),
    (False, 'No leido'),
)

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisor')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    cuerpo = models.CharField(max_length=1000)
    leido = models.BooleanField(choices=LEIDO, default=False)
    fecha = models.DateTimeField(blank=True, null=True, default=datetime.now)

    def __str__(self):

        return self.cuerpo + ' - ' + self.emisor.username + ' - ' + self.receptor.username
