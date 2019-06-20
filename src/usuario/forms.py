from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuario.models import Usuario


class UsuarioCreationFormAdmin(UserCreationForm):
    class Meta(UserCreationForm):
        model = Usuario
        fields = '__all__'


class UsuarioCreationForm(UserCreationForm):
    username = forms.CharField(
        error_messages={
            'required': 'este campo é obrigatório'},
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
            'required': 'Este campo é obrigatório!.'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        ),
        label=''
    )
    password1 = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
            }
        ),
        label='digite sua senha'
    )

    password2 = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
            }
        ),
        label='Digite sua senha novamente'
    )

    foto = forms.ImageField(required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'foto')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Verifique se as senhas são iguais.")
        return password2

    def save(self, commit=True):
        user = super(UsuarioCreationForm, self).save(commit=False)
        user.set_password(user.password)  # set password properly before commit
        if commit:
            user.save()
        return user


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'foto')