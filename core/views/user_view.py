from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models.user import User
from core.serializers.user_serializer import UserSerializer
from core.permissions import IsAdmin

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
