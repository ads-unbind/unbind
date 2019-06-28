from django.shortcuts import render
from artigo.models import Artigo


def index(request):
    artigos = Artigo.objects.order_by('-dataPublicacao')[:2]
    context = {"artigos": artigos}
    return render(request, 'index.html', context)
