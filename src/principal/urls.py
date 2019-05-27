from django.conf.urls import url
from principal import views

#templates tagging
#app_name = 'principal_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
