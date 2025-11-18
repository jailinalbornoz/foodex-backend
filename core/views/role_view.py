from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models.role import Role
from core.serializers.role_serializer import RoleSerializer
from core.permissions import IsAdminOrReadOnly

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
