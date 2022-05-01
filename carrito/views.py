from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Producto
from .carrito import Carrito
from .forms import CarritoAddProducto


# Create your views here.
@require_POST
def carrito_add(request, producto_id):
    carrito = Carrito (request)
    producto = get_object_or_404(Producto, id=producto_id)
    formulario_add = CarritoAddProducto(request.POST)
    if formulario_add.is_valid():
        cd = formulario_add.cleaned_data
        carrito.add(producto=producto, quantity=cd ["cantidad"], update_quantity=cd ["update"])
    return redirect("carrito:carrito_detalle")


def carrito_remove(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.remove(producto)
    return redirect("carrito:carrito_detalle")
    


def carrito_detalle(request):
    carrito = Carrito(request)
    
    for item in carrito:
        item["update_quantity_form"]= CarritoAddProducto(
            initial={"cantidad": item["quantity"], "update": True}
        )
    
    return render(request, "carrito/detalle.html", {"carrito": carrito})

