from django.db import models

class Role(models.Model):
    nombre_rol = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nombre_rol
