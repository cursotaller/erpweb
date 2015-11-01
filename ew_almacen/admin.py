from django.contrib import admin
from ew_almacen.models import Insumo

# Register your models here.


class InsumoAdmin(admin.ModelAdmin):
    search_fields = ('codigo', 'descripcion',)
    list_display = ('codigo', 'descripcion', 'precio')

admin.site.register(Insumo, InsumoAdmin)
