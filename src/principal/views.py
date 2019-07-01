from django.shortcuts import render

from usuario import models
from usuario.models import User
from artigo.models import Artigo
from atividade.models import Atividade


def index(request):
    user = request.user

    if user.is_authenticated:
        usuario = User.objects.get(id=user.id)

        artigo_recomendado = Artigo.objects.order_by('-dataPublicacao').first()
        artigos = Artigo.objects.exclude(id=artigo_recomendado.id).order_by('-dataPublicacao')[:2]

        context = {'usuario': usuario, 'artigos': artigos, 'artigo_recomendado': artigo_recomendado}
        return render(request, 'index.html', context)

    else:
        return render(request, 'index.html')
