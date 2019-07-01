from django.urls import path, re_path
from atividade import views

app_name = 'atividade'

urlpatterns = [
    path('atividades/', views.atividade, name='atividades'),
]
