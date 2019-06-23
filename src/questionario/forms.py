from django import forms
from questionario.models import Questionario, Pergunta

respostas = [(1,1), (2,2), (3,3), (4,4), (5,5)]
#respostas = [1, 2, 3, 4, 5]


class QuestionarioForm(forms.Form):
    pontos = forms.ChoiceField(
        error_messages={
            'required': 'este campo é obrigatório'},
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        choices=respostas,
        label='Em uma escala de 1 a 5 o quanto se identifica com esta afirmação:'
    )

    '''class Meta():
        model = Pergunta
        fields = ('pontos')

    def clean(self):
        all_clean_data = super().clean()
        pontos = all_clean_data['pontos']

        if pontos <= 0 and pontos > 5:
            raise forms.ValidationError(
                "o número tem que estar no interval de 1 e 5")'''
