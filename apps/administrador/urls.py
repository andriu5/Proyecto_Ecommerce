from django.urls import path
from . import views

app_name = 'administrador'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_admin, name='login'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_orders/', views.admin_orders, name='orders'),
]