from django.db import models
from datetime import datetime
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria"

    def __str__(self):
        return self.nombre


class Insumo(models.Model):

    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=60)
    detalle = models.TextField()
    precio = models.FloatField()

    categoria = models.ForeignKey(Categoria, null=True, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"

    def __str__(self):
        return self.descripcion
