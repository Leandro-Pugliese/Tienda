from urllib.request import DataHandler
from django.contrib import admin
from shop.models import *


# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "slug"]
    prepopulated_fields = {"slug": ("nombre",)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = [ "categoria", "nombre", "slug", "precio", "disponibilidad", "fecha_creacion", "fecha_actualizacion" ]
    list_filter = [ "disponibilidad", "fecha_creacion", "fecha_actualizacion" ]
    list_editable = [ "precio", "disponibilidad" ]
    prepopulated_fields = {"slug": ("nombre",)}
