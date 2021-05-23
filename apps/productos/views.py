from django.shortcuts import render, redirect
from django.contrib import messages
from apps.logReg.models import User
import bcrypt
from django.core.paginator import EmptyPage, Paginator

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "master/productos.html")

def dashboard(request):
    #tener cuidado con la seguridad de la pagina!
    if 'admin_loggedin' in request.session and request.session['admin_loggedin'] == True:
        pass
    pass