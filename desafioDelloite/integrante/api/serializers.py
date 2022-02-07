from rest_framework import serializers
from integrante import models

class IntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Integrante
        fields = '__all__'