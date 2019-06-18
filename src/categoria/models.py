from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    #TODO: Colocar descrição da categoria

    def __str__(self):
        return self.nome
