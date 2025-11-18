from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models.role import Role
from .user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    correo_electronico = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)

    id_rol = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)

    is_active = True
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "correo_electronico"
    REQUIRED_FIELDS = ["nombre", "apellido", "rut"]
    # ❗️ NO incluir id_rol aquí

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
