from django import forms
from questionario.models import Questionario, Pergunta, Registro


class QuestionarioForm(forms.ModelForm):
    pontos = forms.IntegerField(
        error_messages={
            'required': 'Este campo é obrigatório!'},
    )

    class Meta:
        model = Registro
        fields = ('pontos',)

    def clean(self):
        all_clean_data = super().clean()
        pontos = all_clean_data['pontos']

        if pontos <= 0 or pontos > 5:
            raise forms.ValidationError("O número tem que estar no interval de 1 e 5!")

    def save(self, id_pergunta, id_user, pontos):
        self.usuario = id_user
        self.pergunta = id_pergunta
        self.pontos = pontos
        super().save()



'''
    def save(self):
        all_clean_data = super().clean()
        pontos = all_clean_data['pontos']

        pergunta_id = Pergunta.objects.get(id=self.pergunta)

        print("save modificado")
        print(pontos)
'''
