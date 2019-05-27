from django.conf.urls import url
from usuario import views

#templates tagging
#app_name = 'principal_app'

urlpatterns = [
    url(r'register/$',views.register,name='register'),
    url(r'login/$',views.login,name='login'),
]
