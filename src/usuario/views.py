from django.shortcuts import render

from usuario.forms import UsuarioCreationForm

from usuario.forms import UsuarioChangeForm

from usuario.models import Usuario
from . import forms
from usuario import models
from django.contrib.auth import login as django_login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout


def register(request):
    if request.method == 'POST':
        register_form = UsuarioCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(request.POST['password1'])
            user.save()

            return HttpResponseRedirect(reverse('questionario'))
        else:
            print(register_form.errors)

    else:
        register_form = UsuarioCreationForm()

    return render(request, 'register.html', {'register_form': register_form})


def login(request):
    context = {'error': ''}
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        usuario = Usuario.objects.get(username=name)
        if usuario.check_password(password) and usuario.is_active:
            django_login(request, usuario)
            return HttpResponseRedirect(reverse('index'))
        else:
            error = 'Login inválido!'
            context = {'error': error}
    return render(request, 'login.html', context)


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return HttpResponseRedirect(reverse('index'))

def questionario(request):
    context = {'error': ''}
    return render(request,'questionario_user.html',context)
