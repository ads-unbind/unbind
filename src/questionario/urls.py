from django.urls import path,re_path
from questionario import views

#templates tagging
#app_name = 'principal_app'

urlpatterns = [
    path('questionario_user/',views.questionario,name='questionario'),
    path('questionario_teste/',views.responde_pergunta,name='responde_questionario'),
    path('questionario_list/',views.respostas_lista,name='respostas_lista'),
]
