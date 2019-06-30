from django.urls import path, re_path
from questionario import views

app_name = 'questionario'

urlpatterns = [    
    path('', views.questionarios, name='lista_questionarios'),
    path('questionario/<int:id>', views.questionario, name='questionario'),
    path('questionario/novo', views.cria_questionario, name='questionario_novo'),
]
