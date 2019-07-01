import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','unbind.settings')

import django
django.setup()

import random
import fake_gen
import sys

from usuario.models import Usuario
from artigo.models import Artigo
from categoria.models import Categoria
from questionario.models import Pergunta
from atividade.models import Atividade
from faker import Faker

fakegen = Faker()

# image = f"{os.getcwd()}{static/images/template/cinema.jpg}"

categorias = [
    'Lazer',
    'Intelecto',
    'Saúde',
    'Vida Financeira',
    'Amigos e Familia',
    'Trabalho e Carreira',
    'Espiritualidade',
    'Amor',
]

def popula_categoria():
    print("Populating categoria...")
    for i in range(8):
        c = Categoria.objects.get_or_create(nome=categorias[i])

def populate(N=5):

    for entry in range(N):
        # Categoria
        cat = add_categoria()

        # atributo de Artigo
        fake_titulo = fakegen.text(max_nb_chars=15)
        fake_text = fakegen.text()
        fake_imagem = sys.path.append(
            '/home/igor/Documents/UnB/2019-1/DES/unbind/src/static/images/template/cinema.jpg'
        )
        fake_autor = fakegen.name()
        fake_curtidas = 3

        # atributo Pergunta
        fake_enunciado = fakegen.text(max_nb_chars=120)
        fake_pontos = random.choice([1, 2, 3, 4, 5])
        # atributo de Questionário
        fake_questionario_nome = fakegen.text(max_nb_chars=15)
        fake_estado = random.choice(
            ['Disponível', 'Indisponível', 'Respondido'])
        # atributo de Atividade
        fake_estado = ''

        # inicializar os objetos

        categ = Categoria.objects.get_or_create(nome=cat)[0]

        artig = Artigo.objects.get_or_create(
            titulo=fake_titulo, texto=fake_text, imagem=fake_imagem, autor=fake_autor, categoria=categ)[0]

        # quest = Questionario.objects.get_or_create(
        #     nome=fake_questionario_nome, estado=fake_estado)[0]

        # perg = Pergunta.objects.get_or_create(
        #     enunciado=fake_enunciado, pontos=fake_pontos, categoria=categ, questionario=quest)[0]

        # ativ = Atividade.objects.get_or_create(
        #     titulo=fake_titulo, descricao=fake_enunciado, dicas=fake_text, estado=fake_estado, pontos=fake_pontos, categoria=categ)[0]


if __name__ == '__main__':
    print("Running script popula...")
    popula_categoria()
    # populate(5)
    print("complete")
