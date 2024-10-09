from rest_framework import serializers

from gestion.models import Auto, Categoria


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class AutoSerializer(serializers.ModelSerializer):
    categoria = CategorySerializer()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Auto
        fields = '__all__'

    def get_description(self, value):
        if value.descripcion is None:
            return "No posee descripcion"
        return value.descripcion
    
    def update(self, instance, validated_data):
        category_data = validated_data.pop(
            'categoria', None
        )

        categoria, _= Categoria.object.get_or_create(
            **category_data
        )

        instance.categoria = categoria
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()

        return instance
