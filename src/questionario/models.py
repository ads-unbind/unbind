from django.db import models

from usuario.models import User
from categoria.models import Categoria


class Questionario(models.Model):
    nome = models.CharField(max_length=30)
    data_resposta = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="respostas"
    )

    def __str__(self):
        return self.nome

    def create_questionario(self, nome, usuario):
        questionario = self.create(nome=nome, usuario=usuario)
        return questionario

    def save(self, usuario):
        self.nome = 'Questionario'
        self.usuario = usuario
        super().save()


class Pergunta(models.Model):
    enunciado = models.CharField(max_length=120)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.enunciado


class Resposta(models.Model):
    resposta = models.IntegerField()
    questionario = models.ForeignKey(
        Questionario, on_delete=models.CASCADE, related_name="respostas")
    pergunta = models.ForeignKey(
        Pergunta, on_delete=models.CASCADE, related_name="respostas")

    def __str__(self):
        return 'Pergunta: {} Resposta: {} '.format(self.pergunta.id, self.resposta)

    def save(self, questionario, pergunta, resposta):
        self.questionario = questionario
        self.pergunta = pergunta
        self.resposta = resposta
        super().save()
