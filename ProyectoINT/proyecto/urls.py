"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from app import views
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.pag_inicio, name = 'pag_inicio'),
    url(r'RegistroUsuario/$', views.RegistroUsuario, name = 'RegistroUsuario'),
    url(r'RegistroCliente/$', views.RegistroCliente, name = 'RegistroCliente'),
    url(r'RegistroProducto/$', views.RegistroProducto, name = 'RegistroProducto'),
    url(r'RegistroCategoria/$', views.RegistroCategoria, name = 'RegistroCategoria'),
    url(r'RegistroVenta/$', views.RegistroVenta, name = 'RegistroVenta'),
    url(r'RegistroSede/$', views.RegistroSede, name = 'RegistroSede'),
    url(r'^UsuarioCreado', views.UsuarioCreado, name = 'UsuarioCreado'),
    url(r'^ClienteCreado', views.ClienteCreado, name = 'ClienteCreado'),
    url(r'^ProductoCreado', views.ProductoCreado, name = 'ProductoCreado'),
    url(r'^CategoriaCreada', views.CategoriaCreada, name = 'CategoriaCreada'),
    url(r'^SedeCreada', views.SedeCreada, name = 'SedeCreada'),
    url(r'^Login/$', views.Login, name = 'Login'),
    url(r'^Logout', views.Logout, name = 'Logout'),
    url(r'^PaginaEncargado', views.PaginaEncargado, name = 'PaginaEncargado'),
]
