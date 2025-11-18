from django.db import models
from .ingrediente import Ingrediente

class Canasta(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, related_name='stock_items')
    cantidad_disponible = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unidad = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Canasta"

    def __str__(self):
        return f"{self.ingrediente.nombre_ing} - {self.cantidad_disponible} {self.unidad}"
