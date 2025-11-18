from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ...models import Receta
from ...serializers import  RecetaSerializer
from ...permissions import IsProfesorOrReadOnly
from ...services import escalar_ingredientes, reconciliar_con_inventario

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().prefetch_related("ingredientes","pasos","autor")
    serializer_class = RecetaSerializer
    permission_classes = [IsProfesorOrReadOnly]

    @action(detail=True, methods=["get"], url_path="scale")
    def scale(self, request, pk=None):
        receta = self.get_object()
        porciones = int(request.query_params.get("porciones", receta.porciones_base))
        return Response(escalar_ingredientes(receta, porciones))

    @action(detail=True, methods=["get"], url_path="recalc-inventario")
    def recalc_inventario(self, request, pk=None):
        receta = self.get_object()
        porciones = int(request.query_params.get("porciones", receta.porciones_base))
        return Response(reconciliar_con_inventario(receta, porciones))
