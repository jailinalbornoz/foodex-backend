from rest_framework import viewsets
from core.permissions import IsProfesorOrAdmin

from core.models.relaciones import (
    RecetaIngrediente, RecetaEtapa, RecetaTecnica, EtapaIngrediente
)
from core.serializers.receta_serializer import (
    RecetaIngredienteSerializer,
    RecetaEtapaSerializer,
    RecetaTecnicaSerializer
)
from core.serializers.etapa_serializer import EtapaIngredienteSerializer


class RecetaIngredienteViewSet(viewsets.ModelViewSet):
    queryset = RecetaIngrediente.objects.all()
    serializer_class = RecetaIngredienteSerializer
    permission_classes = [IsProfesorOrAdmin]


class RecetaEtapaViewSet(viewsets.ModelViewSet):
    queryset = RecetaEtapa.objects.all()
    serializer_class = RecetaEtapaSerializer
    permission_classes = [IsProfesorOrAdmin]


class RecetaTecnicaViewSet(viewsets.ModelViewSet):
    queryset = RecetaTecnica.objects.all()
    serializer_class = RecetaTecnicaSerializer
    permission_classes = [IsProfesorOrAdmin]


class EtapaIngredienteViewSet(viewsets.ModelViewSet):
    queryset = EtapaIngrediente.objects.all()
    serializer_class = EtapaIngredienteSerializer
    permission_classes = [IsProfesorOrAdmin]
