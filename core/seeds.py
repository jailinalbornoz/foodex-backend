from core.models.role import Role
from core.models.user import User


def seed_roles():
    roles = ["Admin", "Profesor", "Alumno"]
    for r in roles:
        Role.objects.get_or_create(nombre_rol=r)


def seed_admin():
    """
    Crea un superusuario automáticamente después de migrar.
    Usa el UserManager correctamente.
    """
    if not User.objects.filter(correo_electronico="admin@foodex.cl").exists():
        User.objects.create_superuser(
            correo_electronico="admin@foodex.cl",
            password="admin123",
            nombre="Admin",
            apellido="Foodex",
            rut="11111111-1",
            id_rol=Role.objects.get(nombre_rol="Admin"),
        )
        print("👑 Superusuario creado: admin@foodex.cl / admin123")
    else:
        print("👑 Superusuario ya existe.")
