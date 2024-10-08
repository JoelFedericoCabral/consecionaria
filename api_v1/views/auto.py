from rest_framework.viewsets import ModelViewSet
from gestion.models import Auto
from api_v1.serializers.auto_serializer import AutoSerializer

class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer






