from django.shortcuts import render,redirect
from usuario.forms import UsuarioForm, UsuarioUpdateForm
from . import forms
from usuario import models
from django.contrib.auth import login as django_login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout

from usuario.models import User


def register(request):
    if request.method == 'POST':
        register_form = UsuarioForm(data=request.POST)

        if register_form.is_valid():
            user = register_form.save()
            user.set_password(user.password)
            user.save()

            return HttpResponseRedirect(reverse('questionario'))
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

def questionario(request):
    context = {'error': ''}
    return render(request,'questionario_user.html',context)


def update_user(request):

    user_atual = request.user

    if user_atual.is_authenticated:

        usuario = User.objects.get(id=user_atual.id)
        update_form = UsuarioUpdateForm(request.POST or None, instance=usuario)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('index'))

        return render(request,'update_user.html',{'update_form':update_form,'usuario':usuario})
    else:
        return HttpResponseRedirect(reverse('index'))

    '''

    if request.method == 'POST':
        update_form = UsuarioUpdateForm(data=request.POST, instance=request.user)

        if update_form.is_valid():
            user = update_form.save()
            user.set_password(user.password)
            user.save()

            return HttpResponseRedirect(reverse('index'))
        else:
            print(update_form.errors)

    else:
        update_form = UsuarioUpdateForm()

    return render(request, 'update_user.html', {'update_form': update_form})
'''
