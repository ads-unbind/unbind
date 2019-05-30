from django.db import models
from django.contrib.auth.models import User

from artigo.models import Artigo
from atividade.models import Atividade
from questionario.models import Questionario
from conquista.models import Conquista


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Adicionais
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='foto_usuario', blank=True)
    scoreTotal = models.IntegerField()
    atividade = models.ManyToManyField(Atividade)
    artigo = models.ManyToManyField(Artigo)
    questionario = models.ManyToManyField(Questionario)
    conquista = models.ManyToManyField(Conquista)

    def __str__(self):
        return self.user.username
