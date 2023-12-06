from django.urls import path
from paginas.views import inicio

urlpatterns = [
    path("", inicio, name="inicio"),
]