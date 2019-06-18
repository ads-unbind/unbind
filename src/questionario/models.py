from django.db import models

from categoria.models import Categoria


class Questionario(models.Model):
    nome = models.CharField(max_length=20)
    dataResposta = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=(('D', 'Disponível'), ('I', 'Indisponível'), ('R', 'Respondido'),))

    def __str__(self):
        return self.nome

    def get_questions(self):
        questions = self.pergunta.all()
        return questions


class Pergunta(models.Model):
    enunciado = models.CharField(max_length=50)
    pontos = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)

    def __str__(self):
        return self.enunciado
