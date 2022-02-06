from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Integrante(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
