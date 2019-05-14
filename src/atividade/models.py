from django.db import models

from categoria.models import Categoria


class Atividade(models.Model):
    titulo = models.CharField(max_length=15)
    descricao = models.CharField(max_length=30)
    dicas = models.TextField()
    estado = models.CharField(max_length=2, choices=(('DI', 'Disponível'), ('I', 'Indisponível'), ('EE', 'Em Espera'),
                                                     ('EA', 'Em Andamento'), ('C', 'Concluída'), ('B', 'Bloqueada'),
                                                     ('DE', 'Desbloqueada'),))
    pontos = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
