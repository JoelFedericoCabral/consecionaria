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
    Serializador para el modelo ModeloAuto, que incluye la marca relacionada.
    """
    marca = MarcaSerializer()

    class Meta:
        model = ModeloAuto
        fields = ['nombre', 'marca']


class AutoSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Auto. 
    Se encarga de manejar las relaciones con los modelos Categoria, Marca, y ModeloAuto.
    """
    categoria = CategorySerializer()  # Se serializa como un objeto completo
    modelo = ModeloAutoSerializer()   # Se serializa el modelo incluyendo la marca
    description = serializers.SerializerMethodField()  # Campo personalizado para la descripción

    class Meta:
        model = Auto
        fields = '__all__'

    def get_description(self, obj):
        """
        Método para retornar una descripción personalizada si está vacía.
        """
        if obj.descripcion is None or obj.descripcion == "":
            return "No posee descripción"
        return obj.descripcion

    def create(self, validated_data):
        """
        Crea una nueva instancia de Auto.
        Gestiona la creación o recuperación de las instancias relacionadas de Categoria, Marca y ModeloAuto.
        """
        categoria_data = validated_data.pop('categoria')
        modelo_data = validated_data.pop('modelo')
        marca_data = modelo_data.pop('marca')

        # Obtener o crear la categoría
        categoria, _ = Categoria.objects.get_or_create(**categoria_data)

        # Obtener o crear la marca y el modelo
        marca, _ = Marca.objects.get_or_create(**marca_data)
        modelo, _ = ModeloAuto.objects.get_or_create(marca=marca, **modelo_data)

        # Crear la instancia de Auto
        auto = Auto.objects.create(categoria=categoria, modelo=modelo, **validated_data)
        return auto

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de Auto existente.
        También maneja la actualización de las instancias relacionadas de Categoria, Marca y ModeloAuto.
        """
        categoria_data = validated_data.pop('categoria', None)
        modelo_data = validated_data.pop('modelo', None)
        marca_data = modelo_data.pop('marca', None) if modelo_data else None

        # Actualizar o crear la categoría
        if categoria_data:
            categoria, _ = Categoria.objects.get_or_create(**categoria_data)
            instance.categoria = categoria

        # Actualizar o crear la marca y el modelo
        if modelo_data:
            if marca_data:
                marca, _ = Marca.objects.get_or_create(**marca_data)
                modelo_data['marca'] = marca
            modelo, _ = ModeloAuto.objects.get_or_create(**modelo_data)
            instance.modelo = modelo

        # Actualizar el resto de los campos
        instance.precio = validated_data.get('precio', instance.precio)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        
        instance.save()
        return instance














# from rest_framework import serializers
# from gestion.models import Auto, Categoria


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Categoria
#         fields = '__all__'


# class AutoSerializer(serializers.ModelSerializer):
#     categoria = CategorySerializer()
#     description = serializers.SerializerMethodField()

#     class Meta:
#         model = Auto
#         fields = '__all__'

#     def get_description(self, value):
#         if value.descripcion is None:
#             return "No posee descripcion"
#         return value.descripcion
    
#     def update(self, instance, validated_data):

#         category_data = validated_data.pop(
#             'categoria', None
#         )

#         categoria, _= Categoria.object.get_or_create(
#             **category_data
#         )

#         instance.categoria = categoria
#         instance.nombre = validated_data.get('nombre', instance.nombre)
#         instance.save()

#         return instance

#     def create(self, validated_data):
#         auto = Auto.objects.create(
#             **validated_data,
#             #nombre = validated_data['nombre'],
#             #precio = validated_data['precio'],
#             #imagen = validated_data['imagen'],
#             #descripcion = validated_data['descripcion'],
#             #marca = validated_data['marca'],
#             #modelo = validated_data['modelo'],
            
#         )
#         return auto