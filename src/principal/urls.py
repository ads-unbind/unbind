from django.urls import path,re_path
from principal import views

#templates tagging
#app_name = 'principal_app'

urlpatterns = [
    path('',views.index,name='index'),
]
