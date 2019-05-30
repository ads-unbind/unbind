from django.urls import path,re_path
from artigo import views

#templates tagging
#app_name = 'principal_app'

urlpatterns = [
    path('usuario_artigo/',views.usuario_artigo,name='usuario_artigo'),
]
