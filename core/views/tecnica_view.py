from rest_framework import viewsets
from core.models.tecnica import Tecnica
from core.serializers.tecnica_serializer import TecnicaSerializer
from core.permissions import IsProfesorOrAdmin

class TecnicaViewSet(viewsets.ModelViewSet):
    queryset = Tecnica.objects.all()
    serializer_class = TecnicaSerializer
    permission_classes = [IsProfesorOrAdmin]
