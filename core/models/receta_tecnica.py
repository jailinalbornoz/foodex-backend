from django.db import models
from .receta import Receta
from .tecnica import Tecnica

class RecetaTecnica(models.Model):
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE, db_column="id_receta")
    id_tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, db_column="id_tecnica")

    class Meta:
        db_table = "receta_tecnica"
        unique_together = ("id_receta", "id_tecnica")
