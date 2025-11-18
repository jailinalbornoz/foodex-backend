from django.db import models
from .receta import Receta
from .ingrediente import Ingrediente

class RecetaIngrediente(models.Model):
    id_receta = models.ForeignKey(Receta, on_delete=models.CASCADE, db_column="id_receta")
    id_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, db_column="id_ingrediente")
    cantidad_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "receta_ingrediente"
        unique_together = ("id_receta", "id_ingrediente")
