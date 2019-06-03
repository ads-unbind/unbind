from django.shortcuts import render
from usuario.forms import UsuarioForm
from . import forms
from usuario import models
from django.contrib.auth import login as django_login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout


def register(request):
    if request.method == 'POST':
        register_form = UsuarioForm(data=request.POST)

        if register_form.is_valid():
            user = register_form.save()
            user.set_password(user.password)
            user.save()

            return HttpResponseRedirect(reverse('login'))
        else:
            print(register_form.errors)

    else:
        register_form = UsuarioForm()

    return render(request, 'register.html', {'register_form': register_form})


def login(request):
    context = {'error': ''}
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if (user is not None and user.is_active):
            django_login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            error = 'Login inválido!'
            context = {'error': error}
    return render(request, 'login.html', context)


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return HttpResponseRedirect(reverse('index'))
