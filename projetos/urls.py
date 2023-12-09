from django.urls import path,include
from projetos.views import inicio,detalhe
from rest_framework import routers
from projetos.views import ProjetoViewSet, detalhe, inicio

router = routers.DefaultRouter()
router.register('api',ProjetoViewSet)

urlpatterns = [
    path("",inicio,name="inicio"),
    path("<int:pk>/",detalhe,name="detalhe"),
    path("api-auth/",include("rest_framework.urls",namespace="rest_framework")),
]
urlpatterns += router.urls
