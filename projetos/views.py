from django.shortcuts import render
from django.http import HttpResponse
from .models import Projeto
from rest_framework import viewsets
from .serializers import ProjetoSerializer
# Create your views here.
class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
def inicio(req) -> HttpResponse:
    projetos = Projeto.objects.all()
    contexto = {"projetos": projetos}
    return render(req, "projetos/inicio.html",contexto)
def detalhe(req,pk):
    projeto = Projeto.objects.filter(id=pk).first()
    contexto = {"projeto":projeto}
    return render(req,"projetos/detalhe.html",contexto)
