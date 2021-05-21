from django.urls import path
from . import views

app_name = 'logReg'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('login/', views.login, name='login'),
    path('verificar_email/', views.verificar_email, name='verificar_email'),
    path('logout/', views.logout, name='logout'),
]