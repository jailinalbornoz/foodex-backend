from django.db import models
from .user import User


class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    nombre_receta = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    tiempo_preparacion_minutos = models.IntegerField(null=True, blank=True)
    porciones = models.IntegerField(null=True, blank=True)
    detalle_montaje = models.TextField(null=True, blank=True)
    justificacion_tecnica = models.TextField(null=True, blank=True)
    justificacion_comercial = models.TextField(null=True, blank=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="usuario_id"
    )

    class Meta:
        db_table = "recetas"

    def __str__(self):
        return self.nombre_receta
