from django.db import models
from .receta import Receta
from .etapa import Etapa
from .ingrediente import Ingrediente
from .tecnica import Tecnica

class RecetaEtapa(models.Model):
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    id_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    orden_etapa = models.IntegerField(null=True, blank=True)


class RecetaIngrediente(models.Model):
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    id_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad_total = models.DecimalField(max_digits=10, decimal_places=2)


class EtapaIngrediente(models.Model):
    id_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    id_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad_etapa = models.DecimalField(max_digits=10, decimal_places=2)


class RecetaTecnica(models.Model):
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    id_tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE)
