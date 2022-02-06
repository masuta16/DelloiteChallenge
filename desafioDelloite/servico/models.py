from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Servico(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ("-created",)

#     def __str__(self):
#         return self.title
# #Essa função irá retornar o endereço dentro do arquivo post_detail com
# #o arquivo slug
#     def get_absolute_url(self):
#         return reverse("blog:detail", kwargs={"slug": self.slug})