from django.shortcuts import render

from usuario import models
from usuario.models import User
from artigo.models import Artigo

def index(request):
    user_atual = request.user

    if user_atual.is_authenticated:
        usuario = User.objects.get(id=user_atual.id)
        artigos = Artigo.objects.order_by('-dataPublicacao')[:2]
        context = {'usuario': usuario, 'artigos': artigos}
        return render(request, 'index.html', context)

    else:
        return render(request, 'index.html')

    
    
