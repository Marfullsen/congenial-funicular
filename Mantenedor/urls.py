from django.urls import path
from . import views
from .views import login, registro, perfil, salir

urlpatterns = [
    path('generar_informe/<slug:informe_de>/<int:parametros>/<slug:tipo>/', views.generar_informe),
    
    # [host]/Mantenedor/...
    path('', views.to_index),
    path('index', views.index, name='index'),
    path('registro_cliente', views.registro_cliente, name='registro_cliente'),
    #path('agregar_cliente', views.agregar_cliente, name='agregar_cliente'),
    path('servicios', views.servicios, name='servicios'),
    path('crear_reserva', views.crear_reserva, name='crear_reserva'),
    path('reservas', views.reservas, name='reservas'),
    path('orden_reparacion', views.orden_reparacion, name='orden_reparacion'),
    path('orden_pedido', views.orden_pedido, name='orden_pedido'),
    path('exportar', views.exportar, name='exportar'),

    path('empleado',views.empleado, name='empleado'),
    path('agregar_empleado', views.agregar_empleado, name='agregar_empleado'),
    path('login/', login, name='login'),

    path('registrar_proveedor',views.registrar_proveedor, name='registrar_proveedor'),
    path('registro_vehiculo',views.registro_vehiculo, name='registro_vehiculo'),
    path('presupuesto',views.presupuesto, name='presupuesto'),

    #path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('perfil/',perfil, name='perfil'),
    path('salir/',salir, name='salir')
]