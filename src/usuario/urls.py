from django.urls import path, re_path
from usuario import views

# app_name = 'principal_app'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registro/', views.register, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/conta/', views.account, name='conta'),
    path('perfil/conta/delete', views.delete, name='delete'),
    path('perfil/senha/', views.change_password, name='senha'),
]
