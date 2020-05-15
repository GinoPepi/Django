from django.db import models

# Create your models here.

class Autor (models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField(primary_key=True)
    def _str_(self):
        return("{} : {}".format(self.codigo, self.nombre))

class Libro (models.Model):
    titulo = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    paginas = models.IntegerField()
    codigo = models.IntegerField(primary_key=True)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, null=True,)
    def _str_(self):
        return ("{} : {}".format(self.codigo, self.titulo))

class Ejemplar (models.Model):
    localizacion = models.CharField(max_length=50)
    codigo = models.IntegerField(primary_key=True)
    localizacion = models.CharField(max_length=50)
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE,null=True,)
    usuarios = models.ManyToManyField('Usuario',)
    def _str_(self):
        return ("{} : {}: Libro:{}".format(self.codigo, self.localizacion, self.libro))

class Usuario (models.Model):
    telefono = models.IntegerField()
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    codigo = models.IntegerField(primary_key=True)
    ejemplares = models.ManyToManyField('Ejemplar',)
    def _str_(self):
        return ("{} : {}: {}".format(self.dodigo, self.nombre, self.telefono))