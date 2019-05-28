from django.urls import path,re_path
from usuario import views

#templates tagging
#app_name = 'principal_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]
