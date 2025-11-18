from django.db import models
from .user import User

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=100)
    tipo = models.CharField(max_length=28, blank=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='recetas')
    porciones_base = models.PositiveIntegerField(default=1)
    tiempo_preparacion_min = models.PositiveIntegerField(default=0)
    detalle_montaje = models.CharField(max_length=255, blank=True)
    url_bosquejo_base = models.CharField(max_length=255, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
