from django.contrib.auth.base_user import BaseUserManager
from core.models.role import Role

class UserManager(BaseUserManager):

    def create_user(self, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError("El usuario debe tener correo electrónico")

        correo_electronico = self.normalize_email(correo_electronico)

        # Si no se asigna rol, se usa ALUMNO por defecto
        if "id_rol" not in extra_fields or extra_fields["id_rol"] is None:
            extra_fields["id_rol"], _ = Role.objects.get_or_create(nombre_rol="ALUMNO")

        user = self.model(correo_electronico=correo_electronico, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_electronico, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Asegurar rol administrador
        admin_role, _ = Role.objects.get_or_create(nombre_rol="ADMIN")
        extra_fields["id_rol"] = admin_role

        return self.create_user(correo_electronico, password, **extra_fields)
