from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from usuario import models
from usuario.models import User
from artigo.models import Artigo
from categoria.models import Categoria


def listar_por_categoria(request, id):
    """
    Método responsável pela listagem de artigos com base na categoria
    :param request: Requisição do usuário
    :param id: Identificador da categoria
    :return: Lista de artigos da categoria
    """
    user = request.user

    if user.is_authenticated:
        usuario = User.objects.get(id=user.id)

        categoria = Categoria.objects.get(id=id)
        artigos = Artigo.objects.filter(categoria=id)
        context = {'usuario': usuario, 'artigos': artigos,
                   'nome_categoria': categoria.nome}

        return render(request, 'artigos.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))


def visualizar(request, id):
    """
    Método responsável pela leitura de artigos
    :param request: Requisição do usuário
    :param id: Identificador do artigo
    :return: Conteúdo do artigo
    """
    user = request.user

    if user.is_authenticated:
        usuario = User.objects.get(id=user.id)

        artigo = Artigo.objects.get(id=id)
        context = {'usuario': usuario, 'artigo': artigo}

        return render(request, 'artigo.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))


def listar_artigos(request):
    """
    Método responsável pela listagem de artigos
    :param request: Requisição do usuário
    :return: Lista de artigos
    """

    user = request.user

    if user.is_authenticated:
        usuario = User.objects.get(id=user.id)

        artigos = Artigo.objects.order_by('-dataPublicacao')
        categorias = Categoria.objects.all()
        context = {'usuario': usuario,
                   'artigos': artigos, 'categorias': categorias}

        return render(request, 'artigos.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))
