from pyexpat import model
from statistics import mode
from rest_framework import viewsets
from post.api import serializers
from post import models

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()