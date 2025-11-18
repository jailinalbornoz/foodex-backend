from django.db import models
from .receta import Receta

class Ingrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='ingredientes')
    nombre_ing = models.CharField(max_length=58)
    tipo_ing = models.CharField(max_length=58, blank=True)
    cantidad_base = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nombre_ing} ({self.cantidad_base} {self.unidad})"
