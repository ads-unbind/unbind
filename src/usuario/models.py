from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from artigo.models import Artigo
from atividade.models import Atividade
from questionario.models import Questionario, Pergunta
from conquista.models import Conquista


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Adicionais
    nome = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='foto_usuario', blank=True, null=True)
    scoreTotal = models.IntegerField(blank=True, null=True)
    atividade = models.ManyToManyField(Atividade)
    artigo = models.ManyToManyField(Artigo)
    questionario = models.ManyToManyField(Questionario)
    conquista = models.ManyToManyField(Conquista)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_usuario(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_usuario(sender, instance, **kwargs):
        instance.usuario.save()

    def get_user_points_last_form_by_category(self, categoriaId):
        ultimoQuestionario = self.questionario.last().id
        perguntasDaCategoria = Pergunta.objects.filter(categoria_id = categoriaId, questionario_id = ultimoQuestionario)
        pontosDaCategoria = 0
        for pergunta in perguntasDaCategoria:
            pontosDaCategoria += pergunta.pontos

        return pontosDaCategoria

    def get_user_xp(self):
        atividades = self.atividade.all()
        xp = 0
        for atividade in atividades:
            xp += atividade.pontos

        return xp
