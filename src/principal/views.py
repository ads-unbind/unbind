from django.shortcuts import render

from usuario import models
from usuario.models import User
from artigo.models import Artigo
from atividade.models import Atividade


def index(request):
    user = request.user

    if user.is_authenticated:
        usuario = User.objects.get(id=user.id)
        artigos = Artigo.objects.order_by('-dataPublicacao')[:2]
        context = {'usuario': usuario, 'artigos': artigos}
        return render(request, 'index.html', context)

    else:
        return render(request, 'index.html')
