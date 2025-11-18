from rest_framework import serializers
from core.models import Receta

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = "__all__"
