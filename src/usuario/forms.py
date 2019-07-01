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

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
