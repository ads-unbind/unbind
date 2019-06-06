import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','unbind.settings')

import django
django.setup()

import random
import fake_gen
import sys

#importando as models
from usuario.models import Usuario
from artigo.models import Artigo
from categoria.models import Categoria
from questionario.models import Pergunta, Questionario

from faker import Faker

fakegen = Faker()

#image = f"{os.getcwd()}{static/profile_image/godfather.jpg}"

categories = ['categorie1','categorie2','categorie3','categorie4','categorie5']

def add_categoria():
    c = Categoria.objects.get_or_create(nome=random.choice(categories))[0]
    c.save()
    return c

def populate(N=5):

    for entry in range(N):
        #atributo de categotia
        cat = add_categoria()
        #atributo de Artigo
        fake_titulo = fakegen.text(max_nb_chars=15)
        fake_text =  fakegen.text()
        fake_imagem = sys.path.append('/static/profile_image/godfather.jpg')
        fake_autor = fakegen.name()
        fake_curtidas = 3
        #atributo Pergunta
        fake_enunciado = fakegen.text(max_nb_chars=50)
        fake_pontos = random.choice([1,2,3,4,5])
        #atributo de Questionário
        fake_questionario_nome = fakegen.text(max_nb_chars=15)
        fake_estado = random.choice(['Disponível', 'Indisponível', 'Respondido'])

        #inicializar os objetos
        categ = Categoria.objects.get_or_create(nome=cat)[0]

        artig = Artigo.objects.get_or_create(titulo=fake_titulo,texto=fake_text,imagem=fake_imagem,autor=fake_autor,curtidas=fake_curtidas,categoria=categ)[0]

        quest = Questionario.objects.get_or_create(nome=fake_questionario_nome,estado=fake_estado)[0]

        perg = Pergunta.objects.get_or_create(enunciado=fake_enunciado,pontos=fake_pontos,categoria=categ,questionario=quest)[0]

if __name__ == '__main__':
    print("populating date")
    populate(5)
    print("complete")
