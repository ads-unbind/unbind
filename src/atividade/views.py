from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from usuario import models
from usuario.models import User
from atividade.models import Atividade
from categoria.models import Categoria


def atividade(request):
    user = request.user

    if user.is_authenticated:

        # atividades = user.usuario.get_user_activities()
        # categorias = Categoria.objects.all()
        # usuario_atividades = []
        # for atividade in atividades:
        #     usuario_atividades.append(atividade)
        # atividades_recomendadas = user.usuario.get_recommended_activities()

        usuario = User.objects.get(id=user.id)

        atividades = Atividade.objects.all()
        categorias = Categoria.objects.all()
        context = {'usuario': usuario,
                   'atividades': atividades, 'categorias': categorias}

        return render(request, 'atividades.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))
