from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *
import time, random, string
from django.db import connection

def pag_inicio(request):
    return render(request, 'Principal.html',{})

def RegistroUsuario(request):
    
    if request.method == "POST":
        form = FormularioRegistroUsuario(request.POST, request.FILES)

        if form.is_valid():
            DPI = form.cleaned_data.get('DPI')
            Nombre = form.cleaned_data.get('Nombre')
            Correo = form.cleaned_data.get('Correo')
            Fecha_Nacimiento = form.cleaned_data.get('Fecha_Nacimiento')
            passw = form.cleaned_data.get('password')

            usu = Usuario.objects.filter(dpi = DPI)
            verificacion = usu.exists()

            if verificacion == False:
                Usuario.objects.create(
                    dpi = DPI,
                    nombre = Nombre,
                    correo = Correo,
                    fecha_nacimiento = Fecha_Nacimiento,
                    password = passw,
                    encargado = 'S'
                )
                return redirect('UsuarioCreado')
            else:
                return render(request, 'RegistroUsuario.html',{"form":form})

    else:
        form = FormularioRegistroUsuario()

    return render(request, 'RegistroUsuario.html',{"form":form})


def RegistroCliente(request):
    
    if request.method == "POST":
        form = FormularioRegistroCliente(request.POST, request.FILES)

        if form.is_valid():
            DPI = form.cleaned_data.get('DPI')
            NIT = form.cleaned_data.get('NIT')
            Nombre = form.cleaned_data.get('Nombre')
            Direccion = form.cleaned_data.get('Direccion')
            Sede = form.cleaned_data.get('Sede')

            print(NIT)
            print(Direccion)
            print(NIT)
            usu = Cliente.objects.filter(dpi = DPI)
            verificacion = usu.exists()

            print(verificacion)
            if verificacion == False:
                print('asdf')
                Cliente.objects.create(
                    dpi = DPI,
                    nombre = Nombre,
                    nit = NIT,
                    direccion = Direccion,
                    sede = Sede
                )
                print('1asdf')
                return redirect('ClienteCreado')
            else:
                return render(request, 'RegistroCliente.html',{"form":form})

    else:
        form = FormularioRegistroCliente()

    return render(request, 'RegistroCliente.html',{"form":form})


def UsuarioCreado(request):
    if request.method == "POST":
        return redirect('Login')
    else:
        return render(request, 'UsuarioCreado.html', {})


def ClienteCreado(request):
    if request.method == "POST":
        return redirect('Login')
    else:
        return render(request, 'ClienteCreado.html', {})

def Logout(request):
    request.session["Usuario"] = ""
    request.session["Encargago"] = ""   
    request.session["Correo"] = ""
    request.session["Password"] = ""
    
    if request.method == "POST":
        return redirect('pag_inicio')
    else:
        return render(request, 'LogOut.html', {})
        
def Login(request):
    if request.method == "POST":
        form = FormularioLogin(request.POST)

        if form.is_valid():
            Correo = form.cleaned_data.get('Correo')
            passw = form.cleaned_data.get('password')
            usu = Usuario.objects.filter(correo = Correo, password = passw)
            verificacion = usu.exists()

            if verificacion == True:

                #las pongo actualmente en las variables de session
                request.session["Usuario"] = usu[0].nombre
                request.session["Encargago"] = usu[0].encargado   
                request.session["Correo"] = usu[0].correo
                request.session["Password"] = usu[0].password

                if usu[0].encargado == 'N':
                    return redirect('PaginaUsuario')
                elif usu[0].encargado == 'S':
                    return redirect('PaginaEncargado')

            else:
                messages.warning(request, 'El usuario no existe.')
    else:
        form = FormularioLogin()

    return render(request, 'Login.html',{"form":form})

def PaginaEncargado(request):
    if "Encargago" in request.session:
        if  request.session["Encargago"] == "S":
            return render(request, 'PaginaEncargado.html',{})
        else:
            return redirect('AccesoDenegado')
    else:
        return redirect('AccesoDenegado')

def AccesoDenegado(request):
    if request.method == "POST":
        return redirect('pag_inicio')
    else:
        return render(request, 'AccesoDenegado.html', {})