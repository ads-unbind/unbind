import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','unbind.settings')

import django
django.setup()

import random
import fake_gen
import sys
import datetime
from django.conf import settings
from django.utils.timezone import make_aware

from usuario.models import Usuario
from artigo.models import Artigo
from categoria.models import Categoria
from questionario.models import Pergunta
from atividade.models import Atividade
from faker import Faker

fake = Faker()

categoria = [
    'Lazer', 'Intelecto', 'Saúde', 'Vida Financeira', 
    'Amigos e Familia', 'Trabalho e Carreira', 'Espiritualidade', 'Amor',
]
enunciado = [
	'Consegue aproveitar os momentos em que você faz aquilo que gosta?',
    'Você tem investido tempo, e buscado evoluir seus conhecimentos?',
	'Sua alimentação é equilibrada, você faz exercícios físicos, não usa drogas (incluindo álcool) e dorme bem?',
	'Você não tem problemas com seu dinheiro, e tem ao menos o suficiente pra ter uma vida confortável?',
	'Sua relação com seus amigos e/ou familiares é muito boa?',
	'Você se sente bem em seu ambiente de trabalho e/ou estudo?',
	'Você é uma pessoa grata com as pessoas que estão ao seu redor, e pelos bens que você já tem?',
    'Você é uma pessoa que se sente amada, e se sente capaz de amar outras pessoas?',
]
image_paths = [
    '../static/images/category/1.jpg',
    '../static/images/category/2.jpg',
    '../static/images/category/3.jpg',
    '../static/images/category/4.jpg',
    '../static/images/category/5.jpg',
    '../static/images/category/6.jpg',
    '../static/images/category/7.jpg',
    '../static/images/category/8.jpg',
]

def get_artigo_info():
    fake_titulo = fake.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None)
    fake_texto = fake.text(max_nb_chars=6000, ext_word_list=None)
    fake_imagem = image_paths[random.randrange(8)]
    fake_autor = fake.name()
    raw_datetime = fake.past_datetime(start_date="-1d", tzinfo=None)
    settings.TIME_ZONE
    fake_datetime = make_aware(raw_datetime)

    artigo = {
        'titulo': fake_titulo,
        'texto': fake_texto,
        'imagem': fake_imagem,
        'autor': fake_autor,
        'data_pub': fake_datetime,
    }

    return artigo

def get_atividade_info():
    fake_titulo = fake.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None)
    fake_descricao = fake.text(max_nb_chars=200, ext_word_list=None)
    fake_dicas = fake.text(max_nb_chars=500, ext_word_list=None)
    fake_imagem = image_paths[random.randrange(8)]

    atividade = {
        'titulo': fake_titulo,
        'descricao': fake_descricao,
        'dicas': fake_dicas,
        'imagem': fake_imagem,
    }

    return atividade

def populate_categorias():
    print("Populating categorias...")
    for i in range(8):
        c = Categoria.objects.get_or_create(nome=categoria[i])

def populate_perguntas():
    print("Populating perguntas...")
    categorias = Categoria.objects.all()

    i=0
    for c in categorias:
        p = Pergunta.objects.get_or_create(
            enunciado=enunciado[i], categoria=c
        )
        i+=1

def populate_artigos():
    print("Populating artigos...")
    categorias = Categoria.objects.all()

    n = len(categorias) * 3
    for i in range(n):
        artigo = get_artigo_info()
        a = Artigo.objects.get_or_create(
            titulo=artigo['titulo'],
            texto=artigo['texto'],
            imagem=artigo['imagem'], 
            autor=artigo['autor'],
            dataPublicacao=artigo['data_pub'], 
            categoria=categorias[i % 3],
        )

def populate_atividades():
    print("Populating atividades...")
    categorias = Categoria.objects.all()

    n = len(categorias) * 3
    for i in range(n):
        atividade = get_atividade_info()
        a = Atividade.objects.get_or_create(
            titulo=atividade['titulo'],
            descricao=atividade['descricao'],
            dicas=atividade['dicas'],
            imagem=atividade['imagem'],
            categoria=categorias[i % 3],
        )

if __name__ == '__main__':
    print("Running populate script...")
    populate_categorias()
    populate_perguntas()
    populate_artigos()
    populate_atividades()
    print("Database succesfully populated!")
