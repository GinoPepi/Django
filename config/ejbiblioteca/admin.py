from django.contrib import admin
from ejbiblioteca.models import Autor
from ejbiblioteca.models import Libro
from ejbiblioteca.models import Ejemplar
from ejbiblioteca.models import Usuario


# Register your models here.
admin.site.register (Autor,)
admin.site.register (Libro,)
admin.site.register (Ejemplar,)
admin.site.register (Usuario,)