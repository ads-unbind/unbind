from django.shortcuts import render

from artigo.models import Artigo

from categoria.models import Categoria


def usuario_artigo(request):
    return render(request, 'usuario_artigo.html')


def listar_por_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    artigos = Artigo.objects.filter(categoria=id)
    context = {"artigos": artigos, "nome_categoria": categoria.nome}

    return render(request, 'artigos.html', context)


def visualizar(request, id):
    artigo = Artigo.objects.get(id=id)
    context = {"artigo": artigo}

    return render(request, 'artigo.html', context)