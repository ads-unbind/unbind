from django.shortcuts import render

from categoria.models import Categoria


def list(request):
    """
    Listagem de Categorias
    :param request: requisição http
    :return: lista de categorias
    """
    categorias = Categoria.objects.all()
    context = {
        "categorias": categorias
    }
    return render(request, 'categorias.html', context)