from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(
        verbose_name="titulo do projeto",
        max_length=100,
        help_text="titulo do projeto",
    )
    descricao = models.TextField(
        verbose_name="descricao do projeto",
        help_text="descricao do projeto",
    )
    tecnologia = models.CharField(
        max_length=20,
        verbose_name="tecnologia usada no projeto",
        help_text="tecnologia usada no projeto"
    )
    class Meta:
        db_table: str = "projeto"
        verbose_name: str = "projeto",
        verbose_name_plural: str = "projetos"