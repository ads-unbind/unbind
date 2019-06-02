from django import forms
from django.contrib.auth.models import User
from usuario.models import Usuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    #username = forms.CharField()
    email = forms.EmailField()
    foto = forms.ImageField()

    class Meta():
        model = Usuario
        fields = ('nome','email','password','foto')
