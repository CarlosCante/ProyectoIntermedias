from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from .models import *
from django.forms.widgets import CheckboxSelectMultiple

from .models import Categoria

class FormularioRegistroUsuario(forms.Form):
    DPI = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Nombre = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Correo = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Fecha_Nacimiento = forms.DateField(required = True,input_formats = ["%d/%m/%Y"], label='Fecha de Nacimiento (DD/MM/YYYY)')
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))

class FormularioRegistroCliente(forms.Form):
    DPI = forms.IntegerField(widget=forms.TextInput(),required = True)
    Nombre = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    NIT = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Direccion = forms.CharField(max_length=100, widget=forms.TextInput(),required = True)
    Sede = forms.IntegerField(widget=forms.TextInput(),required = True)

class FormularioRegistroProducto(forms.Form):
    SKU = forms.CharField(max_length=150,widget=forms.TextInput(),required = True)
    CodigoBarras = forms.CharField(max_length=150, widget=forms.TextInput(),required = True , label="Codigo De Barras")
    Nombre = forms.CharField(max_length=150, widget=forms.TextInput(),required = True)
    Descripcion = forms.CharField(max_length=150, widget=forms.TextInput(),required = True)
    Precio = forms.FloatField(widget=forms.TextInput(),required = True)
    Categori = Categoria.objects.all()

class FormularioRegistroCategoria(forms.Form):
    Nombre = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    
class FormularioLogin(forms.Form):
    Correo = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'), required = True)

class FormularioRegistroSede(forms.Form):
    Alias = forms.CharField(max_length=150, widget=forms.TextInput(),required = True)
    Direccion = forms.CharField(max_length=150, widget=forms.TextInput(),required = True)
    Departamento = forms.CharField(max_length=150, widget=forms.TextInput(),required = True)
    Municipio = forms.CharField(max_length=150, widget=forms.TextInput(),required = True)
    Encargado = forms.CheckboxSelectMultiple()



