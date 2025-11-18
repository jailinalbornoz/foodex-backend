from rest_framework import viewsets
from core.models.canasta import Canasta
from core.serializers.canasta_serializer import CanastaSerializer


class CanastaViewSet(viewsets.ModelViewSet):
    queryset = Canasta.objects.all()
    serializer_class = CanastaSerializer
