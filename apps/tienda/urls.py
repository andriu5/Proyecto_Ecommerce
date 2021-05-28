from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    # path('<imagen>/', views.ProductDetailView.as_view(), name='show_prod'),
    path('show/<int:id>/', views.show_producto, name='show_prod'), # SHOW producto!
    path('carrito/', views.carrito_productos, name='carrito'), # Carrito de compras!
    path('add_carts/', views.agregar_a_carrito, name='agregar_a_carrito'), # Agregando a Carrito de compras!
    path('success/', views.post_checkout, name='confirmacion_compra'), # Carrito de compras!
    path('reset/', views.reset, name='reset'), # Carrito de compras!
    path('delete_item_cart/<int:id>/', views.borrar_del_carrito, name='borrar_del_carrito'), # Carrito de compras!
]