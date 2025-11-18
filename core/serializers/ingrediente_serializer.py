from rest_framework import serializers
from core.models.ingrediente import Ingrediente, CategoriaIngrediente


class CategoriaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaIngrediente
        fields = "__all__"


class IngredienteSerializer(serializers.ModelSerializer):
    categoria = CategoriaIngredienteSerializer(read_only=True)
    id_categoria = serializers.IntegerField(write_only=True)

    class Meta:
        model = Ingrediente
        fields = [
            "id_ingrediente",
            "nombre",
            "unidad",
            "precio_unitario",
            "calorias",
            "categoria",
            "id_categoria",
        ]
