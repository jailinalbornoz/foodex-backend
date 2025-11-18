from rest_framework import serializers
from core.models import Ingrediente, CategoriaIngrediente

class CategoriaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaIngrediente
        fields = "__all__"

class IngredienteSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(
        source="id_categoria.nombre_categoria", read_only=True
    )

    class Meta:
        model = Ingrediente
        fields = [
            "id_ingrediente",
            "nombre",
            "unidad",
            "precio_unitario",
            "calorias",
            "id_categoria",
            "categoria_nombre",
        ]
