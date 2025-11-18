from rest_framework import serializers
from core.models.user import User
from core.models.role import Role

class RoleLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id_rol', 'nombre_rol']
        ref_name = "RoleInUser"

class UserSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField(read_only=True)
    id_rol = RoleLiteSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id_usuario',
            'correo_electronico',
            'nombre',
            'apellido',
            'rut',
            'id_rol',
            'is_active',
            'is_staff'
        ]
        read_only_fields = ('id_usuario', 'is_staff', 'is_active')
