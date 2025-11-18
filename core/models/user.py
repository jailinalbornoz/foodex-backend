from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Role(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)

    class Meta:
        db_table = "rol"

    def __str__(self):
        return self.nombre_rol


class UserManager(BaseUserManager):
    def create_user(self, rut, correo_electronico, contrasena=None, **extra_fields):
        if not rut:
            raise ValueError("El usuario debe tener un RUT")
        if not correo_electronico:
            raise ValueError("El usuario debe tener correo")

        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(
            rut=rut,
            correo_electronico=correo_electronico,
            **extra_fields
        )
        user.set_password(contrasena)
        user.save()
        return user

    def create_superuser(self, rut, correo_electronico, contrasena=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(rut, correo_electronico, contrasena, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, unique=True)
    correo_electronico = models.EmailField(max_length=150, unique=True)
    contrasena = models.CharField(max_length=255)
    id_rol = models.ForeignKey(Role, on_delete=models.CASCADE, db_column="id_rol")

    is_active = True
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = ["correo_electronico"]

    objects = UserManager()

    class Meta:
        db_table = "usuarios"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
