from django.shortcuts import render
from .models import Artigo

def usuario_artigo(request):
    user_atual = request.user
    arr = []
    for i in Artigo.objects.filter(usuario=user_atual.id):
        arr.append(i.titulo)
    context = {'artigos': arr}
    return render(request, 'usuario_artigo.html',context)