from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models.receta import Receta
from core.models.relaciones import (
    RecetaIngrediente, RecetaEtapa, RecetaTecnica
)

from core.serializers.receta_serializer import (
    RecetaSerializer,
    RecetaIngredienteSerializer,
    RecetaEtapaSerializer,
    RecetaTecnicaSerializer,
)

from core.permissions import IsProfesorOrAdmin


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    permission_classes = [IsProfesorOrAdmin]

    @action(detail=True, methods=["get"])
    def detalle_completo(self, request, pk=None):
        receta = self.get_object()
        return Response({
            "receta": RecetaSerializer(receta).data,
            "ingredientes": RecetaIngredienteSerializer(
                RecetaIngrediente.objects.filter(id_receta=pk),
                many=True
            ).data,
            "etapas": RecetaEtapaSerializer(
                RecetaEtapa.objects.filter(id_receta=pk),
                many=True
            ).data,
            "tecnicas": RecetaTecnicaSerializer(
                RecetaTecnica.objects.filter(id_receta=pk),
                many=True
            ).data,
        })
