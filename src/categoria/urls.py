from django.urls import path, re_path

from categoria import views

app_name = 'categoria'

urlpatterns = [
    path('listar/', views.list, name='listar_categorias'),

]
