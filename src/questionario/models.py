from django.db import models

from categoria.models import Categoria
# importando a model Usuario
from usuario.models import User


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
    # pontos = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name="perguntas")

    def __str__(self):
        return self.enunciado


# esta model servirá de classe intermediária()
class Registro(models.Model):
    pontos = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="respostas")
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name="respostas")

    def save(self, id_pergunta, id_user, pontos):
        self.usuario = id_user
        self.pergunta = id_pergunta
        self.pontos = pontos
        super().save()

    def __str__(self):
        return 'Pergunta: {} Usuario: {} '.format(self.pergunta.id, self.usuario.id)
