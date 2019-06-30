from django import forms
from django.contrib.auth.models import User
from usuario.models import Usuario


class UsuarioForm(forms.ModelForm):
    first_name = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
            }
        ),
        label=''
    )
    last_name = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Sobrenome',
            }
        ),
        label=''
    )
    username = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
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
        label=''
    )
    verify_password = forms.CharField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha',
            }
        ),
        label=''
    )

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password', 'verify_password')

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        vpasw = all_clean_data['verify_password']

        if password != vpasw:
            raise forms.ValidationError(
                "Sua senha deve ser igual à confirmação!")

        if len(password) < 8:
            raise forms.ValidationError(
                "Sua senha deve ser maior do que 8 caracteres")


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
