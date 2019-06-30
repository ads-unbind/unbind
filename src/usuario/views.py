from django.shortcuts import render, redirect
from usuario.forms import UsuarioForm, UsuarioUpdateForm
from . import forms
from usuario import models
from django.contrib.auth import login as django_login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout

from usuario.models import User

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def register(request):
    user = request.user
    if not user.is_authenticated:

        if request.method == 'POST':
            register_form = UsuarioForm(data=request.POST)

            if register_form.is_valid():
                user = register_form.save()
                user.set_password(user.password)
                user.save()

                django_login(request, user)

                # TODO: Ir para questionario inicial
                return HttpResponseRedirect(reverse('index'))
            else:
                print(register_form.errors)
        else:
            register_form = UsuarioForm()

        context = {'register_form': register_form}
        return render(request, 'register.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))


def login(request):
    user = request.user
    if not user.is_authenticated:

        context = {}
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

    else:
        return HttpResponseRedirect(reverse('index'))


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return HttpResponseRedirect(reverse('index'))


def account(request):
    user = request.user
    if user.is_authenticated:
        usuario = User.objects.get(id=user.id)

        update_form = UsuarioUpdateForm(request.POST or None, instance=usuario)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('conta'))

        context = {'update_form': update_form, 'usuario': usuario}

        return render(request, 'conta.html', context)

    else:
        return HttpResponseRedirect(reverse('index'))


def delete(request):
    user_atual = request.user

    if user_atual.is_authenticated:
        usuario = User.objects.get(id=user_atual.id)

        if request.method == 'POST':
            usuario.delete()
            return HttpResponseRedirect(reverse('index'))

        context = {'usuario': usuario}

        return render(request, 'delete.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))


def change_password(request):
    user_atual = request.user

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=user_atual)

        if form.is_valid():

            form.save()
            update_session_auth_hash(request, form.user)

            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('senha'))

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)


def perfil(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('conta'))
    else:
        return HttpResponseRedirect(reverse('index'))


# TODO: Remover?
def questionario(request):
    context = {'error': ''}
    return render(request, 'questionario_user.html', context)
