from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from .models import *


def listausuarios():
    usr = USUARIO.objects.all()
    usr2 = []
    for x in range(0, len(usr)):
        usr2.append((usr[x].correo,usr[x].correo))
    return usr2

class FormularioRegistroUsuario(forms.Form):
    DPI = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Nombre = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Correo = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Fecha_Nacimiento = forms.DateField(required = True,input_formats = ["%d/%m/%Y"], label='Fecha de Nacimiento (DD/MM/YYYY)')
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))

class FormularioLogin(forms.Form):
    Correo = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'), required = True)

class FormularioCrearSede(forms.Form):
    Alias = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Direccion = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Departamento = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Municipio = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Encargado = forms.ChoiceField(choices=listausuarios())

class FormularioCrearBodega(forms.Form):
    Nombre = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Direccion = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Encargado = forms.ChoiceField(choices=listausuarios())

class FormularioCrearUsuarioPorEncargado(forms.Form):
    DPI = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Nombre = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Correo = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Fecha_Nacimiento = forms.DateField(required = True,input_formats = ["%d/%m/%Y"], label='Fecha de Nacimiento (DD/MM/YYYY)')
    Password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))
    Vendedor = forms.BooleanField()
    Bodeguero =  forms.BooleanField()
    Repartidor = forms.BooleanField() 
