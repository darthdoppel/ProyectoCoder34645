from django.db import models

# Create your models here.


class persona(models.Model):
    nombre = models.CharField(max_length=80)
    vinculo = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechanac = models.DateField()