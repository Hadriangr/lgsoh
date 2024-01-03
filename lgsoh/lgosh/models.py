
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Usuario(models.Model):
    # Definir campos de usuario según tus necesidades
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

# Agrega más modelos según tus necesidades
