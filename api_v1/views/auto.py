from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
import csv
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend 
from gestion.models import Auto, Marca, Comentario
from api_v1.serializers.auto_serializer import AutoSerializer, ComentarioSerializer, MarcaSerializer
from api_v1.filters import AutoFilter 


class AutoPagination(PageNumberPagination):
    """
    Configuración de la paginación para el listado de autos.
    """
    page_size = 10  # Número de autos por página


class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all().order_by('id')
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




    @action(methods=['get'], detail=False, url_path='download-csv')
    def download_csv(self, request):
        """
        Exportar los datos de los autos a un archivo CSV.
        """
        # Definir el tipo de respuesta y el nombre del archivo
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="autos.csv"'

        # Crear el escritor CSV
        writer = csv.writer(response)
        writer.writerow(["Modelo", "Descripción", "Precio", "Categoría", "Imagen"])

        # Filtrar por categoría si se pasa como parámetro
        categoria = request.query_params.get('categoria', None)
        autos = self.get_queryset()
        if categoria:
            autos = autos.filter(categoria__nombre__icontains=categoria)

        # Escribir las filas en el archivo CSV
        for auto in autos:
            writer.writerow([
                f"{auto.modelo.marca.nombre} {auto.modelo.nombre}",
                auto.descripcion or "Sin descripción",
                auto.precio,
                auto.categoria.nombre if auto.categoria else "No posee",
                auto.imagen.url if auto.imagen else "No tiene imagen"
            ])
        
        return response


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    @action(detail=True, methods=['get'])
    def listar_comentarios_por_auto(self, request, pk=None):
        """
        Endpoint personalizado para obtener comentarios de un auto específico.
        """
        comentarios = Comentario.objects.filter(auto_id=pk)
        serializer = self.get_serializer(comentarios, many=True)
        return Response(serializer.data)
