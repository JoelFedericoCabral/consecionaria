import django_filters
from gestion.models import Auto

class AutoFilter(django_filters.FilterSet):
    # Filtro por categoría
    categoria = django_filters.CharFilter(
        field_name='categoria__nombre', 
        lookup_expr='icontains'
    )
    
    # Filtro por marca (relacionada a través de ModeloAuto)
    marca = django_filters.CharFilter(
        field_name='modelo__marca__nombre',  # Ruta hacia el campo de nombre de la marca
        lookup_expr='icontains'  # Para que el filtro sea insensible a mayúsculas y minúsculas
    )

    class Meta:
        model = Auto
        fields = ['categoria', 'marca']  # Aca podemos añadir otros filtros si quisieramos

