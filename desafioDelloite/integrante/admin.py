from django.contrib import admin

from .models import Integrante

#Nessa função com decorator é passada uma tupla onde tem os \
# campos que o admin mostra no campo prepopulated fields o campo\
#slug sera preenchido automaticamente
@admin.register(Integrante)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "age")
