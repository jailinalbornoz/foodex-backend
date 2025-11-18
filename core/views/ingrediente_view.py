from rest_framework import viewsets
from core.models.ingrediente import Ingrediente
from core.serializers.ingrediente_serializer import IngredienteSerializer
from core.permissions import IsProfesorOrAdmin

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [IsProfesorOrAdmin]
