
from pathlib import Path

from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as iniciarSesion, logout, authenticate

import rut_chile

def to_index(request):
    """Redirección hacia index"""
    return redirect('index')

def login (request):
    formulario = None
    if request.method =='POST':
        formulario = AuthenticationForm(data = request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contra = formulario.cleaned_data['password']
            usuarioLogueado = authenticate(username = usuario, password = contra)

            if usuarioLogueado is not None:
                iniciarSesion(request, usuarioLogueado)
                context = {'perfil':
                            {'nivel':'admin'},
                            'level':'admin'
                            }
                return render(request, 'Mantenedor/perfil.html', context)
                #return render(request,'Mantenedor/perfil.html')
    else:
        formulario = AuthenticationForm()
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'Mantenedor/login.html',
        context
    )

def registro (request):
    formulario = FormularioRegistro()
    if request.method == 'POST':
        formulario = FormularioRegistro(data = request.POST)
        # try:
        #     if not rut_chile.is_valid_rut(formulario['username']):
        #         return render(request, 'Mantenedor/registro.html', {formulario:formulario, 'errores':'rut mal ingresado'})
        # except ValueError:
        #     return render(request, 'Mantenedor/registro.html', {formulario:formulario, 'errores':'rut mal ingresado'})
        if formulario.is_valid():
            usuario_guardado = formulario.save()
            if usuario_guardado is not None:
                iniciarSesion(request,usuario_guardado)
                context = {'perfil':
                            {'nivel':'admin'},
                            'level':'admin'
                            }
                return render(request, 'Mantenedor/perfil.html', context)
                #return redirect('/Mantenedor/perfil')
    else:
        formulario = FormularioRegistro()

    context = {'formulario': formulario}
    return render(request, 'Mantenedor/registro.html', context)

def perfil(request):
    return render(
        request,
        'Mantenedor/perfil.html'
    )

def salir(request):
    logout(request)
    return redirect('/Mantenedor/login')

def index (request):
    context={}
    return render (request, 'mantenedor/index.html',context)


def cliente (request):
    context={}
    return render (request, 'mantenedor/cliente.html',context)

def agregar_cliente(request):
    if request.method == 'POST':

        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_apellido = request.POST['apellido']
        mi_direccion = request.POST['direccion']
        mi_telefono = request.POST['telefono']
        mi_celular = request.POST['celular']
        mi_email = request.POST['email']
        mi_password = request.POST['password']
     
        if mi_rut != "":
            try:
                print("Entrando al try")
                cliente = Cliente()


                id_cliente = Cliente.objects.count()+1
                cliente.rut = mi_rut
                cliente.nombre = mi_nombre
                cliente.apellido = mi_apellido
                cliente.direccion = mi_direccion
                cliente.telefono = mi_telefono
                cliente.celular = mi_celular
                cliente.email = mi_email
                cliente.password = mi_password
                
                User.objects.create_user(mi_nombre,mi_email,mi_password) 

                n_perfil = Perfil.objects.all().count()+1
                perfil = Perfil(n_perfil,1)
                perfil.save()
                id_usuario = UserPerfil.objects.count()+1
                UserPerfil(id_usuario).save()
                
                cliente = Cliente(id_cliente,mi_nombre,mi_apellido,mi_direccion,
                                    mi_telefono,mi_celular,mi_email,mi_password,mi_rut)

                cliente.save()
                
                return render(request, 'mantenedor/mensaje_datos.html', {})

            except cliente.DoesNotExist:
                return render(request, 'mantenedor/mensaje_datos.html', {})

def servicios (request):
    return render (request, 'mantenedor/servicios.html')



def reservas (request):
    servicios = TipoServicio.objects.all()
    context = {'servicios': servicios }
    return render (request, 'mantenedor/reservas.html', context)



def orden_reparacion (request):
    return render (request, 'mantenedor/orden_reparacion.html')

def orden_pedido (request):
    return render (request, 'mantenedor/orden_pedido.html')


def crear_reserva(request):
    if request.method == 'POST':

        mi_fecha = request.POST['fecha']
        mi_hora = request.POST['hora']
        mi_servicio = request.POST['servicio']
        mi_descripcion = request.POST['descripcion']

     
        if mi_fecha != "":
            try:
              
                reserva = Reservas()

                id_reserva = Reservas.objects.count()+1
                reserva.fecha = mi_fecha
                reserva.hora = mi_hora
                print("\n"+mi_servicio)
                reserva.servicio = mi_servicio
                reserva.descripcion = mi_descripcion
    
                reserva = Reservas(id_reserva,mi_servicio,mi_fecha,mi_hora,1,mi_descripcion,5)

                reserva.save()    
                return render(request, 'mantenedor/mensaje_datos.html', {})

            except reserva.DoesNotExist:
                return render(request, 'mantenedor/mensaje_datos.html', {})



def empleado (request):
    cargos = Cargo.objects.all()
    context = {'cargos': cargos }
    return render(request,'Mantenedor/registro_empleado.html',context)


def agregar_empleado(request):
    if request.method == 'POST':

        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_apellido = request.POST['apellido']
        mi_cargo = request.POST['cargo']
        mi_contacto = request.POST['contacto']
        mi_password = request.POST['password']
     
        if mi_rut != "":
            try:
                
                empleado = Empleado()


                id_empleado = Empleado.objects.count()+1
                empleado.rut = mi_rut
                empleado.nombre = mi_nombre
                empleado.apellido = mi_apellido
                empleado.contacto = mi_contacto
                empleado.password = mi_password
                
                User.objects.create_user(mi_rut,mi_contacto,mi_password) 

                # n_perfil = Perfil.objects.all().count()+1
                # perfil = Perfil(n_perfil,1)
                # perfil.save()
                # id_usuario = UserPerfil.objects.count()+1
                # UserPerfil(id_usuario).save()
                
                empleado = Empleado(id_empleado,mi_nombre,mi_apellido,mi_contacto,mi_cargo,
                                    mi_rut,mi_password)

                empleado.save()
                
                return render(request, 'mantenedor/mensaje_datos.html', {})

            except empleado.DoesNotExist:
                return render(request, 'mantenedor/mensaje_datos.html', {})

