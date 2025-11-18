from rest_framework import serializers
from core.models.etapa import Etapa
from core.models.relaciones import EtapaIngrediente
from core.models.ingrediente import Ingrediente
from core.serializers.ingrediente_serializer import IngredienteSerializer


class EtapaIngredienteSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer(read_only=True)
    id_ingrediente = serializers.IntegerField(write_only=True)

    class Meta:
        model = EtapaIngrediente
        fields = [
            "id_etapa",
            "id_ingrediente",
            "cantidad_etapa",
            "ingrediente",
        ]


class EtapaSerializer(serializers.ModelSerializer):
    ingredientes = serializers.SerializerMethodField()

    class Meta:
        model = Etapa
        fields = [
            "id_etapa",
            "nombre_etapa",
            "descripcion",
            "tiempo_minutos",
            "ingredientes",
        ]

    def get_ingredientes(self, obj):
        items = EtapaIngrediente.objects.filter(id_etapa=obj.id_etapa)
        return EtapaIngredienteSerializer(items, many=True).data
