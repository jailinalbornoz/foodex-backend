from django.db import models

class Etapa(models.Model):
    id_etapa = models.AutoField(primary_key=True)
    nombre_etapa = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    tiempo_minutos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre_etapa
