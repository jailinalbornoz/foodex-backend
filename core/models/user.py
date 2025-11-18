from django.contrib.auth.models import AbstractUser
from django.db import models
from .role import Role

class User(AbstractUser):
    rol = models.ForeignKey(Role, on_delete=models.PROTECT, null=True, blank=True)
    semestre = models.IntegerField(null=True, blank=True)
    carrera = models.CharField(max_length=50, null=True, blank=True)
