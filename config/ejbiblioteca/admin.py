from django.contrib import admin
from ejbiblioteca.models import Autor
from ejbiblioteca.models import Libro
from ejbiblioteca.models import Ejemplar
from ejbiblioteca.models import Usuario

class LibroAdmin (admin.ModelAdmin):
    list_display = ('titulo','editorial')

class EjemplarAdmin (admin.ModelAdmin):
    list_filter = ['libro']

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('nombre',)
        }),
        ('Contacto', {
            'fields': ('direccion', 'telefono',)
        }),
    )
    list_display = ['nombre', 'telefono', ]
    list_display_links = ['nombre', 'telefono',]
class EnLineas(admin.TabularInline):
    model = Libro

class AuthorAdmin(admin.ModelAdmin):
    inlines = [EnLineas,]
    search_fields = ['nombre',]
    list_display = ('codigo' , 'nombre')

# Register your models here.
admin.site.register (Autor,AuthorAdmin)
admin.site.register (Libro , LibroAdmin)
admin.site.register (Ejemplar , EjemplarAdmin)
admin.site.register (Usuario, UserAdmin)
