from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from api_v1.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Solo usuarios staff pueden acceder
