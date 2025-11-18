from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .role import Role
from .user_manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, unique=True)
    correo_electronico = models.EmailField(max_length=150, unique=True)
    contrasena = models.CharField(max_length=255)
    id_rol = models.ForeignKey(Role, on_delete=models.CASCADE)

    USERNAME_FIELD = "correo_electronico"
    REQUIRED_FIELDS = ["rut"]

    objects = UserManager()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
