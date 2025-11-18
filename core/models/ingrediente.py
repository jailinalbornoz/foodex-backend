from django.db import models
from .categoria_ingrediente import CategoriaIngrediente

class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=20)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    calorias = models.IntegerField(null=True, blank=True)

    id_categoria = models.ForeignKey(
        CategoriaIngrediente,
        on_delete=models.CASCADE,
        db_column="id_categoria"
    )

    class Meta:
        db_table = "ingredientes"

    def __str__(self):
        return self.nombre
