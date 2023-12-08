from django.contrib import admin
from .models import Projeto
# Register your models here.
class ProjetoAdm(admin.ModelAdmin):
    pass
admin.site.register(Projeto,ProjetoAdm)
