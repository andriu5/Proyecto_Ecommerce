from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('show/<int:id>/', views.show_producto, name='show_prod'), # SHOW producto!
    path('carrito/', views.carrito_productos, name='carrito'), # Carrito de compras!
    path('success/', views.confirmacion_compra, name='confirmacion_compra'), # Carrito de compras!
]