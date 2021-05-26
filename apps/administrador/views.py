from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
#from apps.logReg.models import User
from django.contrib.auth.models import User
#import bcrypt
from time import gmtime, strftime, time, localtime
from datetime import datetime
from django.http import JsonResponse
from django.core.paginator import EmptyPage, Paginator

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "master/admin_login.html")

def login_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if request.user.is_authenticated:
            print(True)
        if user is not None and user.is_superuser:  # si el Usuario Existe!
            # Redirect to a success page.
            login(request, user)
            messages.success(request, ('Usuario ha iniciado sesión correctamente!'))
            request.session['admin'] = {
                'id': user.id,
                'name': user.first_name,
                'lastname': user.last_name
                }
            request.session['admin_loggedin'] = True
            return redirect('administrador:ordenes')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('Error en el inicio de sesión!'))
            return redirect('administrador:index')

@login_required
def admin_ordenes(request):
    #tener cuidado con la seguridad de la pagina!
    if 'admin' in request.session and request.session['admin_loggedin'] == True:
        ordenes = [
            {
                "id":1,
                "cliente" : {"nombre":"Andres", "apellido":"Alvear"},
                "created_at" : "2021/05/21",
                "direccion_facturacion" : "Encomenderos 237, Dpto. 102",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "199,990",
                "estado": "Orden en proceso", #Order in Process
            },
            {
                "id":2,
                "cliente" : {"nombre":"Jorge", "apellido":"Donoso"},
                "created_at" : "2021/05/22",
                "direccion_facturacion" : "Av. Libertador Bernardo O'higgings 1000, Dpto. 200",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "299,990",
                "estado": "Enviado", #Shipped
            },
            {
                "id":3,
                "cliente" : {"nombre":"Victor", "apellido":"Rocco"},
                "created_at" : "2021/05/23",
                "direccion_facturacion" : "Av. Providencia 14, Dpto. 400",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "399,990",
                "estado": "Cancelada", #Cancelled
            },
            {
                "id":4,
                "cliente" : {"nombre":"Milton", "apellido":"Alvear"},
                "created_at" : "2021/05/21",
                "direccion_facturacion" : "Encomenderos 237, Dpto. 102",
                "ciudad_facturacion" : "Viña del Mar",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "499,990",
                "estado": "Orden en proceso", #Order in Process
            },
            {
                "id":5,
                "cliente" : {"nombre":"Daniel", "apellido":"Donoso"},
                "created_at" : "2021/05/22",
                "direccion_facturacion" : "Av. Libertador Bernardo O'higgings 1000, Dpto. 200",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "599,990",
                "estado": "Enviado", #Shipped
            },
            {
                "id":6,
                "cliente" : {"nombre":"Javier", "apellido":"Rocco"},
                "created_at" : "2021/05/23",
                "direccion_facturacion" : "Av. Providencia 14, Dpto. 400",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "699,990",
                "estado": "Cancelada", #Cancelled
            },
        ]
        # Paginamos el dashboard de Ordenes cada 4 elementos usando Paginator
        p = Paginator(ordenes, 4)
        page_num = request.GET.get('dashboard/orders/<int:page>/', 1)
        page = p.page(page_num) # página desde donde comenzamos a mostrar, ósea, si colocamos 2 entregara el id=5 e id=6
        currentUserID = request.session['admin']['id']
        context={
            # 'todasLasOrdenes': Ordenes.objects.all()
            #"todasLasOrdenes": ordenes
            "todasLasOrdenes": page,
            "user": ""
            }
        return render(request, "master/dashboard_orders.html", context)
    # asumiendo que este sistema de Django es muy seguro!
    request.session.clear()
    request.session['admin_bad_loggedin'] = True
    return redirect('administrador:index')

@login_required
def dashboard(request, page):
    #tener cuidado con la seguridad de la pagina!
    if 'admin' in request.session and request.session['admin_loggedin'] == True:
        ordenes = [
            {
                "id":1,
                "cliente" : {"nombre":"Andres", "apellido":"Alvear"},
                "created_at" : "2021/05/21",
                "direccion_facturacion" : "Encomenderos 237, Dpto. 102",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "199,990",
                "estado": "Orden en proceso", #Order in Process
            },
            {
                "id":2,
                "cliente" : {"nombre":"Jorge", "apellido":"Donoso"},
                "created_at" : "2021/05/22",
                "direccion_facturacion" : "Av. Libertador Bernardo O'higgings 1000, Dpto. 200",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "299,990",
                "estado": "Enviado", #Shipped
            },
            {
                "id":3,
                "cliente" : {"nombre":"Victor", "apellido":"Rocco"},
                "created_at" : "2021/05/23",
                "direccion_facturacion" : "Av. Providencia 14, Dpto. 400",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "399,990",
                "estado": "Cancelada", #Cancelled
            },
            {
                "id":4,
                "cliente" : {"nombre":"Milton", "apellido":"Alvear"},
                "created_at" : "2021/05/21",
                "direccion_facturacion" : "Encomenderos 237, Dpto. 102",
                "ciudad_facturacion" : "Viña del Mar",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "499,990",
                "estado": "Orden en proceso", #Order in Process
            },
            {
                "id":5,
                "cliente" : {"nombre":"Daniel", "apellido":"Donoso"},
                "created_at" : "2021/05/22",
                "direccion_facturacion" : "Av. Libertador Bernardo O'higgings 1000, Dpto. 200",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "599,990",
                "estado": "Enviado", #Shipped
            },
            {
                "id":6,
                "cliente" : {"nombre":"Javier", "apellido":"Rocco"},
                "created_at" : "2021/05/23",
                "direccion_facturacion" : "Av. Providencia 14, Dpto. 400",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "699,990",
                "estado": "Cancelada", #Cancelled
            },
            {
                "id":7,
                "cliente" : {"nombre":"Andres", "apellido":"Alvear"},
                "created_at" : "2021/05/21",
                "direccion_facturacion" : "Encomenderos 237, Dpto. 102",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "199,990",
                "estado": "Orden en proceso", #Order in Process
            },
            {
                "id":8,
                "cliente" : {"nombre":"Jorge", "apellido":"Donoso"},
                "created_at" : "2021/05/22",
                "direccion_facturacion" : "Av. Libertador Bernardo O'higgings 1000, Dpto. 200",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "299,990",
                "estado": "Enviado", #Shipped
            },
            {
                "id":9,
                "cliente" : {"nombre":"Victor", "apellido":"Rocco"},
                "created_at" : "2021/05/23",
                "direccion_facturacion" : "Av. Providencia 14, Dpto. 400",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "399,990",
                "estado": "Cancelada", #Cancelled
            },
            {
                "id":10,
                "cliente" : {"nombre":"Milton", "apellido":"Alvear"},
                "created_at" : "2021/05/21",
                "direccion_facturacion" : "Encomenderos 237, Dpto. 102",
                "ciudad_facturacion" : "Viña del Mar",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "499,990",
                "estado": "Orden en proceso", #Order in Process
            },
            {
                "id":11,
                "cliente" : {"nombre":"Daniel", "apellido":"Donoso"},
                "created_at" : "2021/05/22",
                "direccion_facturacion" : "Av. Libertador Bernardo O'higgings 1000, Dpto. 200",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "599,990",
                "estado": "Enviado", #Shipped
            },
            {
                "id":12,
                "cliente" : {"nombre":"Javier", "apellido":"Rocco"},
                "created_at" : "2021/05/23",
                "direccion_facturacion" : "Av. Providencia 14, Dpto. 400",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "699,990",
                "estado": "Cancelada", #Cancelled
            },
            {
                "id":13,
                "cliente" : {"nombre":"Javier", "apellido":"Rocco"},
                "created_at" : "2021/05/23",
                "direccion_facturacion" : "Av. Providencia 14, Dpto. 400",
                "ciudad_facturacion" : "Santiago",
                "pais_facturacion" : "Chile",
                "codigo_postal" : "8320000",
                "total": "699,990",
                "estado": "Cancelada", #Cancelled
            },
        ]
        # Paginamos el dashboard de Ordenes cada 4 elementos usando Paginator
        p = Paginator(ordenes, 4)
        page_num = request.GET.get('dashboard/orders/<int:page>/',page)

        print("\nNúmero de páginas en el Dashboard de administración de Ordenes:", p.num_pages,"\n")

        
        # Si el administrador trata de ir a una página que no existe. ¡Lo forzamos a ir a la página 1!
        try:
            page = p.page(page_num) # página desde donde comenzamos a mostrar, ósea, si colocamos 2 entregara el id=5 e id=6
        except EmptyPage:
            page = p.page(1)
        currentUserID = request.session['admin']['id']
        context={
            # 'all_orders': Order.objects.all()
            #"todasLasOrdenes": ordenes
            "todasLasOrdenes": page,
            "user": User.objects.get(id=currentUserID).first_name
            }
        return render(request, "master/dashboard_orders.html", context)

def cerrar_sesion(request):
    print('*'*100)
    print(f'Cerrando sesion de administrador y redirijiendolo al login...')
    logout(request)
    # Redirect to a success page.
    messages.success(request, ('Usted ha cerrado sesión!'))
    return redirect("administrador:index") # go to root: "/"