from django.shortcuts import render
from atividade.models import Atividade
from django.http import HttpResponseRedirect
from django.urls import reverse
from categoria.models import Categoria
# Create your views here.

def atividade(request):
    user = request.user
    if user.is_authenticated:

        atividades = user.usuario.get_user_activities()
        categorias = Categoria.objects.all()
        usuario_atividades = []
        for atividade in atividades:
            usuario_atividades.append(atividade)
        atividades_recomendadas = user.usuario.get_recommended_activities()

        return render(request, 'atividades.html', {'usuario_atividades': usuario_atividades, 'categorias': categorias,
                                                   'atividades_recomendadas': atividades_recomendadas})
    else:
        return HttpResponseRedirect(reverse('index'))
