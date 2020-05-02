from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *
import time, random, string
from django.db import connection
from datetime import datetime

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

            usu = USUARIO.objects.filter(dpi = DPI)
            verificacion = usu.exists()

            if verificacion == False:
                #Se crea un nuevo usuario

                u = USUARIO(
                    dpi = DPI,
                    nombre = Nombre,
                    correo = Correo,
                    fecha_nacimiento = Fecha_Nacimiento,
                    password = passw,
                )

                #Se guarda el usuario
                u.save()

                #Se obtiene el rol por medio del id del rol requqerido
                rl = ROL.objects.get(id = 3)

                #Se guarda en la tabla ASIG_ROL la instancia del usuario creado
                #y la instancia del rol obtenido
                ar = ASIG_ROL.objects.create(
                    usuario_dpi = u,
                    rol_id = rl,
                )

                #Se guarda la tupla en ASIG_ROL
                ar.save()

                return redirect('UsuarioCreado')
            else:
                return render(request, 'RegistroUsuario.html',{"form":form})

    else:
        form = FormularioRegistroUsuario()

    return render(request, 'RegistroUsuario.html',{"form":form})

def UsuarioCreado(request):
    if request.method == "POST":
        return redirect('Login')
    else:
        return render(request, 'UsuarioCreado.html', {})

def Logout(request):
    request.session["Usuario"] = ""
    request.session["RolAdministrador"] = ""
    request.session["RolVendedor"] = ""
    request.session["RolBodeguero"] = ""
    request.session["RolRepartidor"] = ""
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
            usu = USUARIO.objects.filter(correo = Correo, password = passw)
            verificacion = usu.exists()

            if verificacion == True:

                #busco su rol en el sistema
                #1 administrador
                #2 vendedor 
                #3 bodeguero
                #4 repartidor
                rolusu = ASIG_ROL.objects.filter(usuario_dpi = usu[0].dpi)

                for i in range(0, len(rolusu)):
                    if rolusu[i].rol_id.id == 1:
                        request.session["RolAdministrador"] = 'S'
                    if rolusu[i].rol_id.id == 2:
                        request.session["RolVendedor"] = 'S'
                    if rolusu[i].rol_id.id == 3:
                        request.session["RolBodeguero"] = 'S'
                    if rolusu[i].rol_id.id == 4:
                        request.session["RolRepartidor"] = 'S'
                        

                 #las pongo actualmente en las variables de session
                request.session["Usuario"] = usu[0].nombre
                request.session["Correo"] = usu[0].correo
                request.session["Password"] = usu[0].password

                if rolusu[0].rol_id.id == 1:
                    return redirect('PaginaAdministrador')
                elif rolusu[0].rol_id.id == 2:
                    return redirect('PaginaVendedor')
                elif rolusu[0].rol_id.id == 3:
                    return redirect('PaginaBodeguero')
                elif rolusu[0].rol_id.id == 4:
                    return redirect('PaginaRepartidor')

            else:
                messages.warning(request, 'El usuario no existe.')
    else:
        form = FormularioLogin()

    return render(request, 'Login.html',{"form":form})


def AccesoDenegado(request):
    if request.method == "POST":
        return redirect('pag_inicio')
    else:
        return render(request, 'AccesoDenegado.html', {})

###################################################################################################
####################################VISTAS DE LOS DIFERENTES ROLES#################################

def PaginaAdministrador(request):
    if "RolAdministrador" in request.session:
        if  request.session["RolAdministrador"] == 'S':
            return render(request, 'PaginaAdministrador.html',{})
        else:
            return redirect('AccesoDenegado')
    else:
        return redirect('AccesoDenegado')

def CrearSede(request):
    if "RolAdministrador" in request.session:
        if  request.session["RolAdministrador"] == 'S':
            if request.method == 'POST':
                datos = request.POST
                
                ID = random.randrange(5, 1000000)
                Alias =  datos.get('Alias')
                Direccion = datos.get('Encargado')
                Departamento = datos.get('Departamento')
                Municipio = datos.get('Municipio')
                EncargadoCorreo = USUARIO.objects.get(correo = datos.get('Encargado'))
                
                sde = SEDE.objects.filter(id = ID)
                while sde.exists():
                    ID = random.randrange(5, 1000000)
                    sde = SEDE.objects.filter(id = ID)

                s = SEDE(
                    id = ID,
                    alias = Alias,
                    direccion = Direccion,
                    departamento = Departamento,
                    municipio = Municipio,
                    encargado_dpi = EncargadoCorreo,
                )

                s.save()


                return redirect('CrearSede')
            else:
                form = FormularioCrearSede()
                    
                return render(request, 'Administrador/CrearSede.html', {"form": form})
        else:
            return redirect('AccesoDenegado')
    else:
        return redirect('AccesoDenegado')

def PaginaVendedor(request):
    if "RolVendedor" in request.session:
        if  request.session["RolVendedor"] == 'S':
            return render(request, 'PaginaVendedor.html',{})
        else:
            return redirect('AccesoDenegado')
    else:
        return redirect('AccesoDenegado')

def PaginaBodeguero(request):
    if "RolBodeguero" in request.session:
        if  request.session["RolBodeguero"] == 'S':
            return render(request, 'PaginaBodeguero.html',{})
        else:
            return redirect('AccesoDenegado')
    else:
        return redirect('AccesoDenegado')

def PaginaRepartidor(request):
    if "RolRepartidor" in request.session:
        if  request.session["RolRepartidor"] == 'S':
            return render(request, 'PaginaRepartidor.html',{})
        else:
            return redirect('AccesoDenegado')
    else:
        return redirect('AccesoDenegado')

def PaginaEncargadoSede(request):
    if "RolRepartidor" in request.session or "RolVendedor" in request.session or "RolBodeguero" in request.session:
        if  request.session["RolRepartidor"] == 'S' or request.session["RolVendedor"] == 'S' or request.session["RolBodeguero"] == 'S':
            return render(request, 'PaginaEncargadoSede.html', {})
        else:
            return redirect('AccesoDenegado')
    else:
        return redirect('AccesoDenegado')

def CrearBodega(request):
    if "RolRepartidor" in request.session or "RolVendedor" in request.session or "RolBodeguero" in request.session:
        if  request.session["RolRepartidor"] == 'S' or request.session["RolVendedor"] == 'S' or request.session["RolBodeguero"] == 'S':
            
            usu = USUARIO.objects.get(correo = request.session["Correo"])
            sde = SEDE.objects.filter(encargado_dpi = usu)

            if sde.exists():
                if request.method == 'POST':
                    datos = request.POST
                
                    ID = random.randrange(5, 1000000)
                    Nombre =  datos.get('Nombre')
                    Direccion = datos.get('Direccion')
                    Estado = "Activa"
                    EncargadoBodega = USUARIO.objects.get(correo = datos.get('Encargado'))
                    SedeBodega = SEDE.objects.get(id = sde[0].id)

                    bdg = BODEGA.objects.filter(id = ID)
                    while bdg.exists():
                        ID = random.randrange(5, 1000000)
                        bdg = BODEGA.objects.filter(id = ID)

                    b = BODEGA(
                        id = ID,
                        nombre = Nombre,
                        direccion = Direccion,
                        estado = Estado,
                        encargado_dpi = EncargadoBodega,
                        sede_id = SedeBodega,
                    )

                    b.save()

                    return redirect('CrearBodega')
                else:
                    form = FormularioCrearBodega()
                    return render(request, 'EncargadoSede/CrearBodega.html', {"form": form, "sede": sde[0].alias})
                
            else:
                return redirect('AccesoDenegado')
            
        else:
            return redirect('AccesoDenegado')
    else:
        return redirect('AccesoDenegado')

def CrearUsuarioPorEncargado(request):
    if "RolRepartidor" in request.session or "RolVendedor" in request.session or "RolBodeguero" in request.session:
        if  request.session["RolRepartidor"] == 'S' or request.session["RolVendedor"] == 'S' or request.session["RolBodeguero"] == 'S':
            
            usu = USUARIO.objects.get(correo = request.session["Correo"])
            sde = SEDE.objects.filter(encargado_dpi = usu)

            if sde.exists():
                if request.method == 'POST':
                    datos = request.POST

                    print("Vendedor: " + str(datos.get('Vendedor')))
                    print("Vendedor: " + str(datos.get('Bodeguero')))
                    print("Vendedor: " + str(datos.get('Repartidor')))

                    DPI = datos.get('DPI')
                    Nombre = datos.get('Nombre')
                    Correo = datos.get('Correo')
                    Fecha_Nacimiento = datetime.strptime(datos.get('Fecha_Nacimiento'),"%d/%m/%Y").strftime("%Y-%m-%d") 
                    passw = datos.get('Password')

                    usu = USUARIO.objects.filter(dpi = DPI)
                    verificacion = usu.exists()

                    if verificacion == False:
                        #Se crea un nuevo usuario

                        u = USUARIO(
                            dpi = DPI,
                            nombre = Nombre,
                            correo = Correo,
                            fecha_nacimiento = Fecha_Nacimiento,
                            password = passw,
                        )

                        #Se guarda el usuario
                        u.save()

                        #2 vendedor 
                        #3 bodeguero
                        #4 repartidor

                        if str(datos.get('Vendedor')) == "on":
                            rlv = ROL.objects.get(id = 2)
                            arv = ASIG_ROL.objects.create(
                                usuario_dpi = u,
                                rol_id = rlv,
                            )
                            arv.save()
                        
                        if str(datos.get('Bodeguero')) == "on":
                            rlb = ROL.objects.get(id = 3)
                            arb = ASIG_ROL.objects.create(
                                usuario_dpi = u,
                                rol_id = rlb,
                            )
                            arb.save()
                        
                        if str(datos.get('Repartidor')) == "on":
                            rlr = ROL.objects.get(id = 4)
                            arr = ASIG_ROL.objects.create(
                                usuario_dpi = u,
                                rol_id = rlr,
                            )
                            arr.save()

                        return redirect('CrearUsuarioPorEncargado')
                    else:
                        return redirect('CrearUsuarioPorEncargado')

                else:
                    form = FormularioCrearUsuarioPorEncargado()
                    return render(request, 'EncargadoSede/CrearUsuarioPorEncargado.html', {"form": form, "sede": sde[0].alias})
                
            else:
                return redirect('AccesoDenegado')
            
        else:
            return redirect('AccesoDenegado')
    else:
        return redirect('AccesoDenegado')
