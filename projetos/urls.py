from django.urls import path
from projetos.views import inicio,detalhe
urlpatterns = [
    path("",inicio,name="inicio"),
    path("<int:pk>/",detalhe,name="detalhe")
]
