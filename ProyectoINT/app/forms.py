from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from .models import *

class FormularioRegistroUsuario(forms.Form):
    DPI = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Nombre = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Correo = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    Fecha_Nacimiento = forms.DateField(required = True,input_formats = ["%d/%m/%Y"], label='Fecha de Nacimiento (DD/MM/YYYY)')
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))

class FormularioLogin(forms.Form):
    Correo = forms.CharField(max_length=50, widget=forms.TextInput(),required = True)
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'), required = True)