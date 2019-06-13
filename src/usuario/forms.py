from django import forms
from django.contrib.auth.models import User
from usuario.models import Usuario

class UsuarioForm(forms.ModelForm):
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
    password = forms.CharField(
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

    verify_password = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
            }
        ),
        label='digite sua senha novamente'
    )

    foto = forms.ImageField(required=False)

    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'verify_password', 'foto')

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        vpasw = all_clean_data['verify_password']

        if password != vpasw:
            raise forms.ValidationError("verifique se as senhas são iguais")

        if len(password) < 6:
            raise forms.ValidationError("a senha tem que ter mais de 6 caracteres ")

class UsuarioUpdateForm(forms.ModelForm):
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
    '''
    password = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
            }
        ),
        label='entre com a nova senha'
    )

    verify_password = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
            }
        ),
        label='confirme sua nova senha'
    )
    '''
    foto = forms.ImageField(required=False)

    class Meta():
        model = User
        fields = ('username', 'email', 'foto')

    '''
    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        vpasw = all_clean_data['verify_password']

        if password != vpasw:
            raise forms.ValidationError("verifique se as senhas são iguais")

        if len(password) < 6:
            raise forms.ValidationError("a senha tem que ter mais de 6 caracteres ")
    '''
