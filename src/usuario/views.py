from django.shortcuts import render
from usuario.forms import UsuarioForm
from . import forms
from usuario import models

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
