from django.urls import path, re_path
from usuario import views

# app_name = 'principal_app'

urlpatterns = [
    path('registro/', views.register, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
]
