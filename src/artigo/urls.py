from django.conf.urls import url
from artigo import views

#templates tagging
#app_name = 'principal_app'

urlpatterns = [
    url(r'usuario_artigo/$',views.usuario_artigo,name='usuario_artigo'),
]
