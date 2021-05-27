from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/<int:page>/', views.dashboard, name='dashboard'),
    path('dashboard/add_prod/', views.admin_productos, name='admin_productos'),
    path('add_prod/', views.add_producto, name='add_prod'),
    path('<int:id>/', views.edit_producto, name='edit_prod'), #EDIT producto!
    path('update/<int:id>/', views.update_producto, name='update_prod'), #UPDATE producto!
    path('<int:id>/destroy/', views.delete_producto, name='delete_prod'), # DELETE producto!
    path('<int:id>/info/', views.info_producto, name='info_prod'), # INFO producto!
]