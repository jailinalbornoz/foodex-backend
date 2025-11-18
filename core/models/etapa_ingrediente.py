from django.db import models
from .etapa import Etapa
from .ingrediente import Ingrediente

class EtapaIngrediente(models.Model):
    id_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, db_column="id_etapa")
    id_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, db_column="id_ingrediente")
    cantidad_etapa = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "etapa_ingrediente"
        unique_together = ("id_etapa", "id_ingrediente")
