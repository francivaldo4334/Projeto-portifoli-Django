from django.shortcuts import render
from django.http import HttpResponse
from .models import Projeto
# Create your views here.
def inicio(req) -> HttpResponse:
    projetos = Projeto.objects.all()
    contexto = {"projetos": projetos}
    return render(req, "projetos/inicio.html",contexto)
def detalhe(req,pk):
    projeto = Projeto.objects.filter(id=pk).first()
    contexto = {"projeto":projeto}
    return render(req,"projetos/detalhe.html",contexto)
