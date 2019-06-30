from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from operator import itemgetter
from artigo.models import Artigo
from atividade.models import Atividade
from questionario.models import Questionario, Pergunta
from conquista.models import Conquista
from categoria.models import Categoria

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")

    # Adicionais
    nome = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='foto_usuario', blank=True, null=True)
    scoreTotal = models.IntegerField(blank=True, null=True)
    atividade = models.ManyToManyField(Atividade, blank = True)
    artigo = models.ManyToManyField(Artigo, blank = True)
    conquista = models.ManyToManyField(Conquista, blank = True)
    #colocando questionário e pergunta na model de usuário
    questionario = models.ManyToManyField(Questionario)
    pergunta = models.ManyToManyField(Pergunta)


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
        atividades = self.atividade.filter(estado = "C")
        xp = 0
        for atividade in atividades:
            xp += atividade.pontos

        return xp

    def get_user_activities(self):
        atividades = self.atividade.filter(estado = "DI")

        return atividades

    def get_user_rewards(self):
        conquistas = self.conquista.filter(disponivel = True)

        return conquistas

    def get_recommended_activities(self):
        categorias = Categoria.objects.all()
        #categoriasDict = {}
        menorPontuacao = 100
        for categoria in categorias:
            pontos = self.get_user_points_last_form_by_category(categoria.id)
            if pontos < menorPontuacao:
                menorPontuacao = pontos
                categoriaRecomendada = categoria

            #categoriasDict[categoria] = pontos
        atividadesRecomendadas = self.atividade.filter(estado = "DI", categoria = categoriaRecomendada)
        #categoriaRecomendada = min(categoriasDict.items(), key=itemgetter(1))
        #sorted_dict = sorted(categoriasDict.items(), key=lambda kv: kv[1])
        #atividades = self.atividade.filter(categoria_id = sorted_dict.value())
        return atividadesRecomendadas

    def get_user_activities_by_category(self, category):
        atividades = self.atividade.filter(estado = "DI", categoria_id = category)

        return atividades

    def suggest_articles(self):
        """
        Calcula a pontuação do usuário em todos os questionários realizados e identifica a categoria ideal do usuário.
        A partir desta categoria, são indicados artigos relacionados.
        :return: lista de artigos relacionados.
        """
        categorias = Categoria.objects.all()
        pontuacao_categorias = {}

        # Cria um dicionário com todas as categorias como chave e iniciadas com valor 0
        for categoria in categorias:
            pontuacao_categorias[categoria.nome] = 0

        # Itera sobre todos os questionários, sobre todas as perguntas, somando a pontuação de cada uma na categoria correta
        for questionario in self.questionario.all():
            for pergunta in questionario.perguntas.all():
                pontuacao_categorias[pergunta.categoria.nome] += pergunta.pontos  # Somando na categoria correta

        pontuacao_max_categoria = max(pontuacao_categorias, key=pontuacao_categorias.get)
        print(pontuacao_max_categoria)  # categoria com a maior pontuação deste usuário

        categoria_ideal = Categoria.objects.get(nome=pontuacao_max_categoria)  # Busca a categoria ideal a partir do nome
        artigos = Artigo.objects.filter(categoria=categoria_ideal).all()  # Busca todos os artigos relacionados a categoria ideal

        return artigos

