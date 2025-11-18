from rest_framework import viewsets
from ...models import Ingrediente
from ...serializers import IngredienteSerializer
from ...permissions import IsProfesorOrReadOnly

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [IsProfesorOrReadOnly]
