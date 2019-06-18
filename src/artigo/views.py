from django.shortcuts import render

from artigo.models import Artigo

from categoria.models import Categoria


def usuario_artigo(request):
    return render(request, 'usuario_artigo.html')


def listar_por_categoria(request, id):
    """
    Método responsável pela listagem de artigos com base na categoria
    :param request: Requisição do usuário
    :param id: Identificador da categoria
    :return: Lista de artigos da categoria
    """
    categoria = Categoria.objects.get(id=id)
    artigos = Artigo.objects.filter(categoria=id)
    context = {"artigos": artigos, "nome_categoria": categoria.nome}

    return render(request, 'artigos.html', context)


def visualizar(request, id):
    """
    Método responsável pela leitura de artigos
    :param request: Requisição do usuário
    :param id: Identificador do artigo
    :return: Conteúdo do artigo
    """
    artigo = Artigo.objects.get(id=id)
    context = {"artigo": artigo}

    return render(request, 'artigo.html', context)


def listar_artigos(request):
    """
    Método responsável pela listagem de artigos
    :param request: Requisição do usuário
    :return: Lista de artigos
    """

    artigos = Artigo.objects.all()
    context = {"artigos": artigos}

    return render(request, 'artigos.html', context)