from django.contrib import admin
from .models import Servico
# Register your models here.
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}