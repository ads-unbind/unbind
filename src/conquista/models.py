from django.db import models

class Conquista(models.Model):
    
    nomeConquista = models.CharField(max_length=50)
    valor = models.IntegerField
    disponivel = models.BooleanField(default = False)
    conteudo = models.FileField(upload_to='conquista/')

    def __str__(self):
        return self.nomeConquista