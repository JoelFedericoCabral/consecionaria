from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from gestion.models import Auto
from api_v1.serializers.auto_serializer import AutoSerializer


class AutoPagination(PageNumberPagination):
    """
    Configuración de la paginación para el listado de autos.
    """
    page_size = 10  # Número de autos por página


class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    pagination_class = AutoPagination

    def destroy(self, request, *args, **kwargs):
        """
        Sobreescribe el método destroy para personalizar la lógica de eliminación.
        - Muestra un mensaje personalizado al eliminar un auto.
        - Gestiona el caso cuando no se encuentra el auto.
        """
        try:
            # Obtener la instancia del auto a eliminar
            instance = self.get_object()
        except Auto.DoesNotExist:
            # Manejo de excepción cuando no se encuentra el auto
            raise NotFound("El auto no existe.")
        
        # Ejecutar la eliminación del auto
        self.perform_destroy(instance)

        # Retornar la respuesta personalizada
        return Response({
            "message": f'El auto {instance.modelo.marca.nombre} {instance.modelo.nombre} ha sido eliminado exitosamente.'
        }, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        """
        Método auxiliar que realiza la eliminación de la instancia.
        """
        instance.delete()



# EJEMPLO DE CREATE CON MSJ PERSONALIZADO QUE NO UTILIZARE EN ESTE PROYECTO


    # def create(self, request, *args, **kwargs):
    #     # Delega la creación al serializador
    #     response = super().create(request, *args, **kwargs)
        
    #     # Aqui podemos modificar la respuesta
    #     return Response({
    #         'message': 'Auto creado exitosamente',
    #         'data': response.data
    #     }, status=status.HTTP_201_CREATED)


        







