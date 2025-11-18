from rest_framework import serializers
from core.models import User, Role


class UserSerializer(serializers.ModelSerializer):
    nombre_rol = serializers.CharField(source="id_rol.nombre_rol", read_only=True)

    class Meta:
        model = User
        fields = [
            "usuario_id",
            "nombre",
            "apellido",
            "rut",
            "correo_electronico",
            "contrasena",
            "id_rol",
            "nombre_rol",
        ]
        extra_kwargs = {
            "contrasena": {"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            **validated_data
        )
        user.set_password(validated_data["contrasena"])
        user.save()
        return user
