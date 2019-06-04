from django import forms
from questionario.models import Questionario,Pergunta

class QuestionarioForm(forms.ModelForm):
    pontos = forms.IntegerField(
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

    class Meta():
        model = Pergunta
        fields = ('pontos')

    def clean(self):
        all_clean_data = super().clean()
        pontos = all_clean_data['pontos']

        if pontos <= 0 and pontos > 5:
            raise forms.ValidationError("o número tem que estar no interval de 1 e 5")
