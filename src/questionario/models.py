from django.db import models


class Questionario(models.Model):
    nome = models.CharField(max_length=20)
    dataResposta = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=(('D', 'Disponível'), ('I', 'Indisponível'), ('R', 'Respondido'),))
    score = models.IntegerField()

    def __str__(self):
        return self.nome
