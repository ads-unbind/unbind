from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from questionario.models import Questionario, Pergunta, Resposta


class RespostaForm(forms.ModelForm):
    resposta = forms.IntegerField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nota de 0 a 10',
            }
        ),
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
    )

    class Meta():
        model = Resposta
        fields = ('resposta',)

    def __init__(self, n, *args, **kwargs):
        super(RespostaForm, self).__init__(*args, **kwargs)
        for i in range(1, n):
            self.fields["resposta%d" % i] = forms.IntegerField(
                error_messages={
                    'required': 'Este campo é obrigatório!'},
                widget=forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Nota de 0 a 10',
                    }
                ),
                validators=[
                    MaxValueValidator(10),
                    MinValueValidator(0)
                ],
            )

    def clean(self):
        all_clean_data = super().clean()
        resposta = all_clean_data['resposta']

        if resposta < 0 or resposta > 10:
            raise forms.ValidationError(
                "O número tem que estar no intervalo de 0 e 10!"
            )

#     def save(self, id_pergunta, id_user, pontos):
#         print(id_pergunta)
#         print(pontos)
#         self.usuario = id_user
#         self.pergunta = id_pergunta
#         self.pontos = pontos
#         super().save()
