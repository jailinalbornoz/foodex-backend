from rest_framework import viewsets
from ...models import PasoProcedimiento
from ...serializers import PasoProcedimientoSerializer
from ...permissions import IsProfesorOrReadOnly

class PasoViewSet(viewsets.ModelViewSet):
    queryset = PasoProcedimiento.objects.all()
    serializer_class = PasoProcedimientoSerializer
    permission_classes = [IsProfesorOrReadOnly]