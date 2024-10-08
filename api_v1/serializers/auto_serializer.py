from rest_framework import serializers

from gestion.models import Auto


class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'

