from django.shortcuts import render
from usuario.forms import UsuarioForm
from . import forms
from usuario import models
from django.contrib.auth import login as django_login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout

def register(request):
    #form = forms.UsuarioForm()

    if request.method == 'POST':
        usuario_form = UsuarioForm(data=request.POST)#to pegando info do form

        if usuario_form.is_valid():
            user = usuario_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(usuario_form.errors)

    else:
        usuario_form = UsuarioForm()

        '''
            print("validation success")
            print("username:"+form.cleaned_data['username'])
            print("email:"+form.cleaned_data['email'])
            print("password:"+form.cleaned_data['password'])
            print("done")
        '''

    return render(request,'register.html',{'usuario_form':usuario_form})


def login(request):
    context = {'error': ''}
    if (request.method == 'POST'):
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