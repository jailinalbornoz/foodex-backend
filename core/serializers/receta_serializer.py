from rest_framework import serializers
from core.models.receta import Receta
from core.models.relaciones import (
    RecetaIngrediente,
    RecetaEtapa,
    RecetaTecnica,
)
from core.models.ingrediente import Ingrediente
from core.models.etapa import Etapa
from core.models.tecnica import Tecnica
from core.serializers.ingrediente_serializer import IngredienteSerializer
from core.serializers.etapa_serializer import EtapaSerializer
from core.serializers.tecnica_serializer import TecnicaSerializer


class RecetaIngredienteSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer(read_only=True)
    id_ingrediente = serializers.IntegerField(write_only=True)

    class Meta:
        model = RecetaIngrediente
        fields = [
            "id_receta",
            "id_ingrediente",
            "cantidad_total",
            "ingrediente",
        ]


class RecetaEtapaSerializer(serializers.ModelSerializer):
    etapa = EtapaSerializer(read_only=True)
    id_etapa = serializers.IntegerField(write_only=True)

    class Meta:
        model = RecetaEtapa
        fields = [
            "id_receta",
            "id_etapa",
            "orden_etapa",
            "etapa",
        ]


class RecetaTecnicaSerializer(serializers.ModelSerializer):
    tecnica = TecnicaSerializer(read_only=True)
    id_tecnica = serializers.IntegerField(write_only=True)

    class Meta:
        model = RecetaTecnica
        fields = [
            "id_receta",
            "id_tecnica",
            "tecnica",
        ]


class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = "__all__"
