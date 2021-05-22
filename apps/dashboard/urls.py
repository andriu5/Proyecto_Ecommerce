from django.urls import path
from . import views

#app_name = 'dashboard'

urlpatterns = [
    path('dashboard/orders/', views.admin_dashboard, name='admin_dashboard'),
]