from rest_framework import viewsets
from ...models import Canasta
from ...serializers import CanastaSerializer
from ...permissions import IsProfesorOrReadOnly

class CanastaViewSet(viewsets.ModelViewSet):
    queryset = Canasta.objects.all()
    serializer_class = CanastaSerializer
    permission_classes = [IsProfesorOrReadOnly]
