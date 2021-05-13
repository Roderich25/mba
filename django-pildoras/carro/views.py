from tienda.models import Producto
from .carro import Carro
from django.shortcuts import redirect


def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect('tienda:tienda')


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect('tienda:tienda')


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)
    return redirect('tienda:tienda')


def limpiar_carro(request):
    carro = Carro(request)
    carro.vaciar()
    return redirect('tienda:tienda')