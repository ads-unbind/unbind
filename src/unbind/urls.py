"""unbind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include, path, re_path
from principal.views import index
from unbind import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('principal.urls')),
    path('', include('usuario.urls')),
    path('artigo/', include('artigo.urls', namespace='artigo')),
    path('questionario/', include('questionario.urls')),
    path('atividade/', include('atividade.urls', namespace='atividade')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
