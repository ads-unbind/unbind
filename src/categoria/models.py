from django.db import models

from questionario.models import Questionario


class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
