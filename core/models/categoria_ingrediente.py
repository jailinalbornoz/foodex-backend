from django.db import models

class CategoriaIngrediente(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "categorias_ingrediente"

    def __str__(self):
        return self.nombre_categoria
