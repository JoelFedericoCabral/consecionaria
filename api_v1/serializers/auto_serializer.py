from rest_framework import serializers
from gestion.models import Auto, Categoria, Cliente, Marca, Comentario, ModeloAuto


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ModeloAutoSerializer(serializers.ModelSerializer):
    marca = serializers.StringRelatedField()

    class Meta:
        model = ModeloAuto
        fields = ['nombre', 'marca']  # Incluimos la marca para que aparezca en el modelo

class AutoSerializer(serializers.ModelSerializer):
    categoria = CategorySerializer(read_only=True)  
    modelo = ModeloAutoSerializer(read_only=True)   
    marca = MarcaSerializer(read_only=True)        
    
    # Campos write_only para aceptar nombres (strings) al crear o actualizar
    categoria_nombre = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(), slug_field='nombre', write_only=True, label="Categoria"
    )
    modelo_nombre = serializers.SlugRelatedField(
        queryset=ModeloAuto.objects.all(), slug_field='nombre', write_only=True, label="Modelo"
    )
    marca_nombre = serializers.SlugRelatedField(
        queryset=Marca.objects.all(), slug_field='nombre', write_only=True, label="Marca"
    )

    class Meta:
        model = Auto
        fields = [
            'id', 'categoria', 'categoria_nombre', 'modelo', 'modelo_nombre',
            'marca', 'marca_nombre', 'precio', 'imagen', 'descripcion'
        ]

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
        """
        categoria = validated_data.pop('categoria_nombre')
        modelo = validated_data.pop('modelo_nombre')
        marca = validated_data.pop('marca_nombre')

        auto = Auto.objects.create(
            categoria=categoria,
            modelo=modelo,
            marca=marca,
            **validated_data
        )
        return auto

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de Auto existente.
        """
        instance.categoria = validated_data.get('categoria_nombre', instance.categoria)
        instance.modelo = validated_data.get('modelo_nombre', instance.modelo)
        instance.marca = validated_data.get('marca_nombre', instance.marca)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)

        instance.save()
        return instance

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'auto', 'autor', 'comentario', 'fecha']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'