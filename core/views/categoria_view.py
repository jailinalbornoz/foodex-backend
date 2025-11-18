from rest_framework import viewsets
from core.models.ingrediente import CategoriaIngrediente
from core.serializers.ingrediente_serializer import CategoriaIngredienteSerializer
from core.permissions import IsAdminOrReadOnly


class CategoriaIngredienteViewSet(viewsets.ModelViewSet):
    queryset = CategoriaIngrediente.objects.all()
    serializer_class = CategoriaIngredienteSerializer
    permission_classes = [IsAdminOrReadOnly]
