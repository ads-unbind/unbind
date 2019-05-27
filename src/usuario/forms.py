from django import forms
from django.contrib.auth.models import User
from usuario.models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioChangeForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()
    email = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a marca do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Email',
            }
        )
    )

    name = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a descrição do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Nome',
            }
        )
    )

    class Meta():
        model = User
        fields = ('username','email','name','password', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmar Senha"
        self.fields['name'].label = "Nome"

    def save(self, commit=True):
        instance = super(CustomUserCreationForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','email','password')
