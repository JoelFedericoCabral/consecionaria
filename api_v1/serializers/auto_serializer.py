from rest_framework import serializers
from gestion.models import Auto, Categoria, Marca, ModeloAuto

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Categoria.
    """
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Marca.
    """
    class Meta:
        model = Marca
        fields = '__all__'

class ModeloAutoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo ModeloAuto.
    """
    class Meta:
        model = ModeloAuto
        fields = ['nombre']  # Solo incluye el campo nombre, sin la relación con la marca

class AutoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Auto.
    En este serializador, se utilizan PrimaryKeyRelatedField para poder seleccionar
    las categorías, modelos y marcas desde un listado desplegable (dropdown).
    """
    # Utilizamos PrimaryKeyRelatedField para permitir la selección en el formulario
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    modelo = serializers.PrimaryKeyRelatedField(queryset=ModeloAuto.objects.all())
    marca = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all())
    
    description = serializers.SerializerMethodField()  # Campo personalizado para la descripción

    class Meta:
        model = Auto
        fields = ['id', 'categoria', 'modelo', 'marca', 'precio', 'imagen', 'descripcion', 'description']

    def get_description(self, obj):
        """
        Método para retornar una descripción personalizada si está vacía.
        """
        if not obj.descripcion:
            return "No posee descripción"
        return obj.descripcion

    def create(self, validated_data):
        """
        Crea una nueva instancia de Auto.
        No necesitamos crear manualmente las relaciones aquí, ya que usamos PrimaryKeyRelatedField.
        """
        return Auto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de Auto existente.
        """
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.marca = validated_data.get('marca', instance.marca)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance
