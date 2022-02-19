from django.shortcuts import render, get_object_or_404
from shop.models import *


# Create your views here.

def inicio(request):
    return render(request, "shop/productos/inicio.html")



def lista_producto(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponibilidad=True)
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        productos = productos.filter(categoria=categoria)
    return render(request, "shop/productos/lista.html", 
    {
        "categoria": categoria, 
        "categorias": categorias, 
        "productos": productos
    })

def detalle_producto(request, id, slug):
    producto = get_object_or_404(
        producto,
        id=id,
        slug=slug,
        disponibilidad=True
    )

    return render(request, "shop/productos/detalle.html",
    {
        "producto": producto
    })
