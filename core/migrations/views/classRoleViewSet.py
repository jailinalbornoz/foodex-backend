from rest_framework import viewsets
from ...models import Role
from ...serializers import RoleSerializer
from ...permissions import IsProfesorOrReadOnly

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsProfesorOrReadOnly]