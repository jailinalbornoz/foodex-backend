from django.db import models
from .receta import Receta

class PasoProcedimiento(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='pasos')
    orden_procedimiento = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=255)

    class Meta:
        ordering = ['orden_procedimiento']
        unique_together = ('receta', 'orden_procedimiento')

    def __str__(self):
        return f"{self.receta.nombre_receta} - Paso {self.orden_procedimiento}"
