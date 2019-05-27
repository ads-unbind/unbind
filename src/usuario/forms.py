from django import forms
from django.contrib.auth.models import User
from usuario.models import Usuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','email','password')
