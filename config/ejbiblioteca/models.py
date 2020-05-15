from django.db import models

# Create your models here.

class Autor (models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField(primary_key=True)

class Libro (models.Model):
    titulo = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    paginas = models.IntegerField()

class Ejemplar (models.Model):
    localizacion = models.CharField(max_length=50)

class Usuario (modesl.Model):
    telefono = models.IntegerField()
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)