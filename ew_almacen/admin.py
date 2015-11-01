from django.contrib import admin
from ew_almacen.models import Insumo, Categoria

# Register your models here.

admin.site.register(Categoria)


class InsumoAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'descripcion',)
    list_display = ('codigo', 'descripcion', 'precio', 'categoria')

admin.site.register(Insumo, InsumoAdmin)
