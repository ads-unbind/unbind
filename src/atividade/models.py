from django.db import models

from categoria.models import Categoria


class Atividade(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    dicas = models.TextField()
    imagem = models.ImageField(upload_to='imagem_atividade', blank=True)
    # pontos = models.IntegerField()

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

