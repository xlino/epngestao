"""gestao_clientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path
#from clientes import urls as clientes_urls
#from django.urls import path, include

#urlpatterns = [
#    path('clientes/', include(clientes_urls)),
#    path('admin/', admin.site.urls),
#]
from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from home import urls as home_urls
#from blog import urls as blog_urls
#from moeda import urls as moeda_urls
#from projetos import urls as projetos_urls
#from controle import urls as controle_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
#from projetos import urls as projetos_urls

urlpatterns = [
    path('', include(home_urls)),
    #path('moeda/',include(moeda_urls)),
    #path('controle/', include(controle_urls)),
    #path('projetos/', include(projetos_urls)),
    #path('blog/', include(blog_urls)),
    #path('clientes/', include(clientes_urls)),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

