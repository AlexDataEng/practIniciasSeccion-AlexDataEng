from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=255)
    tipoUsuario = models.CharField(max_length=50, default='default_value')
    contrasena = models.CharField(max_length=255)  

class Productos(models.Model):
    codigo = models.IntegerField(default=0)
    lote = models.IntegerField(default=0)
    producto = models.CharField(max_length=255)
    totalFacturado = models.IntegerField(default=0)
    totalDevuelto = models.IntegerField(default=0)