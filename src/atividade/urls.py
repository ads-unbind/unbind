from django.urls import path, re_path
from atividade import views


urlpatterns = [
    path('atividades/', views.atividade, name='atividade'),
]
