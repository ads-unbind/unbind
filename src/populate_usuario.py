import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','unbind.settings')

import django
django.setup()

import random
#importando as models
from usuario.models import Usuario
from artigo.models import Artigo
from categoria.models import Categoria

from faker import Faker

fakegen = Faker()
'''
image = f"{os.getcwd()}{static/profile_image/godfather.jpg}"

def add_image():
    t = Image.objects.get_or_create(image)[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        imagem = add_image()

        fake_name = fakegen.name()
        fake_email = fakegen.email()
        fake_password=fakegen.text()
        fake_image = fakegen.ImageField()

        #new entry
        user = User.objects.get_or_create(nome=fake_name,email=fake_email,password=fake_password,foto=imagem)[0]
'''
categories = ['categorie1','categorie2','categorie3','categorie4','categorie5']

def add_categoria():
    c = Categoria.objects.get_or_create(nome=random.choice(categories))[0]
    c.save()
    return c

def populate(N=5):

    for entry in range(N):

        cat = add_categoria()

        categoria = Categoria.objects.get_or_create(nome=cat)[0]

        #acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]#ele vai ter o mesmo nome que o webpg

if __name__ == '__main__':
    print("populating date")
    populate(20)
    print("complete")
