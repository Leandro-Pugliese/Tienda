from django.urls import URLPattern, path
from shop import views

app_name = "shop"

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('productos', views.lista_producto, name = " Lista_Productos"),
    path('<slug:categoria_slug>/', views.lista_producto, name = "Producto_por_Categoria"),
    path('<int:id>/<slug:slug>/', views.detalle_producto, name = "Detalle_Producto"),
]

