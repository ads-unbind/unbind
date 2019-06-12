from django.urls import path,re_path
from artigo import views

#templates tagging
app_name = 'artigo'

urlpatterns = [
    path('usuario_artigo/', views.usuario_artigo, name='usuario_artigo'),
    path('categoria/<int:id>', views.listar_por_categoria, name='listar_por_categoria'),
]
