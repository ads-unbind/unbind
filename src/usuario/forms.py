from django import forms
from django.contrib.auth.models import User
from usuario.models import Usuario


class UsuarioForm(forms.ModelForm):
    username = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório! Preencha este campo com a descrição do produto.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Usuário',
            }
        ),
        label=''
    )
    email = forms.EmailField(
        error_messages={
            'required': 'Este campo é obrigatório! Preencha este campo com a descrição do produto.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        ),
        label=''
    )
    password = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório! Preencha este campo com a descrição do produto.'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
            }
        ),
        label=''
    )
    foto = forms.ImageField(required=False)

    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'foto')
