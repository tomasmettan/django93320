from django.contrib import admin
from home.models import Pintura
# Register your models here.

# admin.site.register(Pintura)

@admin.register(Pintura)
class PinturaAdmin(admin.ModelAdmin):
    # Columna visibles en el listado de registros
    list_display = ("nombre", "fecha_creacion")

    # Campo que funciona como link para entrar al detalle/registro
    list_display_links = ("nombre",)

    # Habilita la barra de busqueda de registros
    search_fields = ("nombre", "autor")

    # Agrega el panel lateral de filtros
    list_filter = ("fecha_creacion",)

    # Determina el orden de los registros
    ordering = ("nombre", "autor", "fecha_creacion")

    # Campo visible pero no editable en el panel de admin
    readonly_fields = ("fecha_creacion",)