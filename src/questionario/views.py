from django.shortcuts import render
from questionario import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from questionario.models import Pergunta
#from forms import QuestionarioForm

# Create your views here.
def questionario(request):

    perguntas = []
    for pergunta in Pergunta.objects.all():
        perguntas.append(pergunta)

    return render(request, 'questionario_user.html', {'perguntas': perguntas})
'''
def chama_form(request):
    if request.method == 'POST':
        questionario_form = QuestionarioForm(data=request.POST)

        if questionario_form.is_valid():
            pontos = questionario_form.save()

        else:
            print(questionario_form.errors)

    else:
        questionario_form = QuestionarioForm()

    return render(request, 'questionario_user.html', {'questionario_form': questionario_form})
'''
