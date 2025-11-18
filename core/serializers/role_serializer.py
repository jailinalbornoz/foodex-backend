from rest_framework import serializers
from core.models.role import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id_rol', 'nombre_rol']
        ref_name = "RoleBase"
