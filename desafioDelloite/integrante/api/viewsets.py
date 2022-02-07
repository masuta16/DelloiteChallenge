from pyexpat import model
from statistics import mode
from rest_framework import viewsets
from integrante.api import serializers
from integrante import models

class IntegranteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IntegranteSerializer
    queryset = models.Integrante.objects.all()