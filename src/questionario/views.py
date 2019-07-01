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

        context = {'usuario': usuario}
        return render(request, 'questionarios.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))


def questionario(request, id):
    # usar id (questionario)
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

                return HttpResponseRedirect(reverse('index'))
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


# def questionario(request):
#     user = request.user
#     if user.is_authenticated:
#         print("autenticado ", user.username)
#         perguntas = []
#         # imprimindo as perguntas
#         questionario = Questionario.objects.filter(id=1)

#         if questionario:

#             for pergunta in questionario[0].perguntas.all():
#                 perguntas.append(pergunta)

#             if request.method == 'POST':

#                 questionario_form = QuestionarioForm(
#                     len(perguntas)-1, data=request.POST)

#                 if questionario_form.is_valid():
#                     i = 0
#                     registros = []
#                     respostas = []
#                     for form in questionario_form:
#                         respostas.append(form.data)
#                     for pergunta in perguntas:
#                         pontos = respostas[i]

#                         registros.append(Registro())
#                         registros[i].save(pergunta, request.user, pontos)
#                         i = i + 1

#                     return HttpResponseRedirect(reverse('index'))
#                 else:
#                     print(QuestionarioForm.errors)
#             questionario_form = QuestionarioForm(len(perguntas)-1)

#             return render(request, 'questionario_user.html', {'perguntas': perguntas, 'questionario_form': questionario_form})
#         else:
#             return HttpResponse("questionario nao existe")
#     else:
#         return HttpResponseRedirect(reverse('index'))


# def responde_pergunta(request):
#     questionario = Questionario.objects.filter(id=1)[0]

#     # Receber formulario que possui uma lista de pontuações e suas respectivas perguntas.
#     # iterar sobre todas as respostas presentes no formulário, dessa forma:

#     # questionario_forms é uma lista de respostas
#     # for pergunta in questionario_forms:
#     for pergunta in questionario.perguntas.all():
#         # resposta = pergunta.resposta
#         resposta = str(
#             input('Digite sua resposta da pergunta {}'.format(pergunta.id)))
#         registro = Registro()
#         registro.save(pergunta, request.user, resposta)


# def respostas_lista(request):
#     user = request.user

#     respostas = Registro.objects.filter(usuario=user)

#     for resposta in respostas:
#         print(resposta.pergunta.enunciado, ": ", resposta.pontos)
#     print('INDICANDO ARTIGOS:')

#     artigos = suggest_articles(user)

#     for artigo in artigos:
#         print(artigo)


# def listar_perguntas_com_maior_pontuacao(request):
#     respostas = Registro.objects.all()
#     # ordenar lista de respostas com base no atributo 'pontos'
