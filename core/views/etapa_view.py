from rest_framework import viewsets
from core.models.etapa import Etapa
from core.serializers.etapa_serializer import EtapaSerializer
from core.permissions import IsProfesorOrAdmin

class EtapaViewSet(viewsets.ModelViewSet):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer
    permission_classes = [IsProfesorOrAdmin]
