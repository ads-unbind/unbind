from django.urls import path,re_path
from artigo import views

#templates tagging
app_name = 'artigo'

urlpatterns = [
    path('categoria/<int:id>', views.listar_por_categoria, name='listar_por_categoria'),
    path('<int:id>', views.visualizar, name='visualizar_artigo'),
    path('lista', views.listar_artigos, name='listar_artigos'),
]
