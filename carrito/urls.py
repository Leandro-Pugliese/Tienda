from django.urls import path
from . import views

app_name = "carrito"

urlpatterns = [
    path("", views.carrito_detalle, name="carrito_detalle"),
    path("add/<int:producto_id>/", views.carrito_add, name="carrito_add"),
    path("remove/<int:producto_id>/", views.carrito_remove, name="carrito_remove"),
]