from django.urls import path, re_path
from principal import views

#app_name = 'principal_app'

urlpatterns = [
    path('', views.index, name='index'),
]
