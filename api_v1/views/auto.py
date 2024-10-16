from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend 
from gestion.models import Auto
from api_v1.serializers.auto_serializer import AutoSerializer
from api_v1.filters import AutoFilter 

class AutoPagination(PageNumberPagination):
    """
    Configuración de la paginación para el listado de autos.
    """
    page_size = 10  # Número de autos por página

class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = [AllowAny]  # Permitir momentáneamente acceso a todos los usuarios
    pagination_class = AutoPagination

    # Habilitar el filtrado
    filter_backends = [DjangoFilterBackend]  # Activar DjangoFilterBackend para filtrar
    filterset_class = AutoFilter  # Asignar la clase de filtro que creamos

    def destroy(self, request, *args, **kwargs):
        """
        Sobreescribe el método destroy para personalizar la lógica de eliminación.
        """
        try:
            instance = self.get_object()
        except Auto.DoesNotExist:
            raise NotFound("El auto no existe.")
        
        self.perform_destroy(instance)

        return Response({
            "message": f'El auto {instance.modelo.marca.nombre} {instance.modelo.nombre} ha sido eliminado exitosamente.'
        }, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        """
        Método auxiliar que realiza la eliminación de la instancia.
        """
        instance.delete()




        







