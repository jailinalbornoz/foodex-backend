from rest_framework import serializers
from core.models.canasta import Canasta
from core.models.ingrediente import Ingrediente


class CanastaSerializer(serializers.ModelSerializer):
    ingrediente_detalle = serializers.SerializerMethodField()

    class Meta:
        model = Canasta
        fields = ["id", "ingrediente", "ingrediente_detalle", "cantidad_disponible", "unidad"]

    def get_ingrediente_detalle(self, obj):
        return {
            "id": obj.ingrediente.id_ingrediente,
            "nombre": obj.ingrediente.nombre,
            "unidad": obj.ingrediente.unidad,
            "categoria": obj.ingrediente.id_categoria.nombre_categoria
        }
