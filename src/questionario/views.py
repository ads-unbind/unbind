from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from usuario.models import User
from questionario import models
from questionario.models import Pergunta, Questionario, Resposta
from questionario.forms import RespostaForm


def questionarios(request):
    user = request.user
    if user.is_authenticated:
        usuario = User.objects.get(id=user.id)
        questionarios = Questionario.objects.filter(usuario=user)

        context = {'usuario': usuario, 'questionarios': questionarios}
        return render(request, 'questionarios.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))


def questionario(request, id):
    # TODO: validar se usuario é autor do questionario
    user = request.user
    if user.is_authenticated:
        usuario = User.objects.get(id=user.id)

        context = {'usuario': usuario}
        return render(request, 'questionario.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))


def cria_questionario(request):
    user = request.user
    if user.is_authenticated:
        usuario = User.objects.get(id=user.id)
        questionario = Questionario()

        perguntas = Pergunta.objects.order_by('categoria', 'id')

        if request.method == 'POST':
            respostas_form = RespostaForm(
                len(perguntas), data=request.POST
            )

            if respostas_form.is_valid():
                questionario.save(user)

                registros = []
                for registrado in respostas_form:
                    registros.append(registrado.data)

                i = 0
                respostas = []
                for pergunta in perguntas:
                    resposta = registros[i]
                    respostas.append(Resposta())
                    respostas[i].save(questionario, pergunta, resposta)
                    i += 1

                return HttpResponseRedirect(reverse('questionario:questionarios'))
            else:
                print(RespostaForm.errors)

        respostas_form = RespostaForm(len(perguntas))
        context = {
            'usuario': usuario,
            'perguntas': perguntas,
            'respostas_form': respostas_form
        }
        return render(request, 'questionario_novo.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))