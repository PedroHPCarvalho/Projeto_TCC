"""
Configuração de URLs para o projeto mysite.

A lista `urlpatterns` direciona URLs para as views correspondentes. Para mais informações, consulte:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

Exemplos:
Views baseadas em função:
    1. Adicione um import:  from my_app import views
    2. Adicione uma URL:  path('', views.home, name='home')
Views baseadas em classe:
    1. Adicione um import:  from other_app.views import Home
    2. Adicione uma URL:  path('', Home.as_view(), name='home')
Incluindo outro arquivo de URLs:
    1. Importe a função include(): from django.urls import include, path
    2. Adicione uma URL:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Inclui as URLs do app gest_financeira na raiz do site (ex: /)
    path('', include('gest_financeira.urls')), # /home ficará na raiz

    # Inclui as URLs do app usuarios também na raiz (ex: /login/, /signup/)
    path('', include('usuarios.urls')),   # /usuarios/login/ e /usuarios/signup/

    # URL para acessar o painel administrativo do Django
    path('admin/', admin.site.urls),
]
