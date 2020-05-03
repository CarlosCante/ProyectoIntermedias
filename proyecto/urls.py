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
    url(r'^UsuarioCreado', views.UsuarioCreado, name = 'UsuarioCreado'),
    url(r'^Login/$', views.Login, name = 'Login'),
    url(r'^Logout', views.Logout, name = 'Logout'),
    url(r'^PaginaAdministrador/$', views.PaginaAdministrador, name = 'PaginaAdministrador'),
    url(r'^PaginaAdministrador/CrearSede', views.CrearSede, name = 'CrearSede'),
    url(r'^PaginaAdministrador/ModificarRoles', views.ModificarRoles, name = 'ModificarRoles'),
    url(r'^PaginaAdministrador/CrearProducto', views.CrearProducto, name = 'CrearProducto'),
    url(r'^PaginaAdministrador/VerProductos', views.VerProductos, name = 'VerProductos'),
    url(r'^PaginaAdministrador/VerSedes', views.VerSedes, name = 'VerSedes'),
    url(r'^PaginaVendedor', views.PaginaVendedor, name = 'PaginaVendedor'),
    url(r'^PaginaBodeguero', views.PaginaBodeguero, name = 'PaginaBodeguero'),
    url(r'^PaginaRepartidor', views.PaginaAdministrador, name = 'PaginaRepartidor'),
    url(r'^AccesoDenegado', views.AccesoDenegado, name = 'AccesoDenegado'),
    url(r'^PaginaEncargadoSede/$', views.PaginaEncargadoSede, name = 'PaginaEncargadoSede'),
    url(r'^PaginaEncargadoSede/CrearBodega', views.CrearBodega, name = 'CrearBodega'),
    url(r'^PaginaEncargadoSede/CrearUsuarioPorEncargado', views.CrearUsuarioPorEncargado, name = 'CrearUsuarioPorEncargado'),
    url(r'^PaginaEncargadoSede/EstadoBodega', views.EstadoBodega, name = 'EstadoBodega'),
]