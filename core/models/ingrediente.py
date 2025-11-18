from django.db import models


class CategoriaIngrediente(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "categorias_ingrediente"

    def __str__(self):
        return self.nombre_categoria


class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=20)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    calorias = models.IntegerField(null=True, blank=True)
    id_categoria = models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE)

    class Meta:
        db_table = "ingredientes"

    def __str__(self):
        return self.nombre
