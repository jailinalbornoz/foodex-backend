from django.db import models
from .receta import Receta
from .etapa import Etapa

class RecetaEtapa(models.Model):
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE, db_column="id_receta")
    id_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, db_column="id_etapa")
    orden_etapa = models.IntegerField()

    class Meta:
        db_table = "receta_etapa"
        unique_together = ("id_receta", "id_etapa")
