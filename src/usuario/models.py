from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Adicionais
    nome = models.CharField(max_length=50)
    dtNascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='foto_usuario', blank=True)

    def __str__(self):
        return self.user.username
