from django.urls import path
from . import views

app_name = 'administrador'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_admin, name='login'),
    path('dashboard/orders/<int:page>/', views.dashboard, name='dashboard'),
    path('admin_ordenes/', views.admin_ordenes, name='ordenes'),
    path('admin_productos/', views.admin_productos, name='productos'),
]