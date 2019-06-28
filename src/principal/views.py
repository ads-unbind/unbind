from django.shortcuts import render
from artigo.models import Artigo
from usuario import models


def index(request):
    artigos = Artigo.objects.order_by('-dataPublicacao')[:2]
    context = {"artigos": artigos}
    return render(request, 'index.html', context)
