from django.db import models

class Tecnica(models.Model):
    id_tecnica = models.AutoField(primary_key=True)
    nombre_tecnica = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "tecnica"

    def __str__(self):
        return self.nombre_tecnica
