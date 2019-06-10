from django.shortcuts import render
from .models import Artigo
from usuario.models import Usuario

def usuario_artigo(request):
    user_atual = request.user
    arr = []
    us = Usuario.objects.filter(user = user_atual.id)
    for i in Artigo.objects.filter(usuario=us[0].id):
        arr.append(i.titulo)
    context = {'artigos': arr}
    return render(request, 'usuario_artigo.html',context)