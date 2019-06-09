from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def usuario_artigo(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'usuario_artigo.html')
    else:
        return HttpResponseRedirect(reverse('index'))
