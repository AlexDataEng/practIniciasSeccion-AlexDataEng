from django.db import models

# Create your models here.

class Sesion(models.Model):
    nombres = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=255)