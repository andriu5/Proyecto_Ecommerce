from django.shortcuts import render, redirect
from django.contrib import messages
from apps.logReg.models import User
import bcrypt
from time import gmtime, strftime, time, localtime
from datetime import datetime
from django.http import JsonResponse
from django.core.paginator import EmptyPage, Paginator

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "master/admin_login.html")

def login_admin(request):
    if request.POST['logAdmin'] == 'login':
        errors = User.objects.log_admin_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('administrador:index')
        else:
            # ver si el nombre de usuario proporcionado existe en la base de datos
            admin = User.objects.filter(email=request.POST['email']) # ¿Por qué usamos el filtro aquí en lugar de get?
            if admin: # tenga en cuenta que aquí aprovechamos la veracidad: una lista vacía devolverá falso
                logged_admin = admin[0] 
                admin = User.objects.get(email = request.POST['email'])
                request.session['admin'] = {
                    'id': admin.id,
                    'nombre': admin.nombre,
                    'apellido': admin.apellido
                }
                # asumiendo tenemos un usuario con este nombre de usuario, éste sería el primero en la lista que obtenemos
                # por supuesto, deberíamos tener cierta lógica para evitar duplicados de nombres cuando creamos usuarios
                # usa el método check_password_hash de bcrypt, pasando el hash de nuestra base de datos y la contraseña del formulario
                if bcrypt.checkpw(request.POST['password'].encode(), logged_admin.password.encode()):
                # si obtenemos True después de validar la contraseña, podemos poner la identificación del usuario en la sesión
                    request.session['admin_id'] = logged_admin.id
                    request.session['admin_loggedin'] = True
                    # ¡Nunca renderices en una publicación, siempre redirigir!
                    return redirect('administrador:ordenes')
            # si no encontramos nada en la base de datos buscando por nombre de usuario o si las contraseñas no coinciden, 
            # redirigir a una ruta segura
            return redirect('administrador:index')

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
        
        context={
            # 'todasLasOrdenes': Ordenes.objects.all()
            #"todasLasOrdenes": ordenes
            "todasLasOrdenes": page
            }
        return render(request, "master/dashboard_orders.html", context)
    request.session.clear()
    request.session['admin_bad_loggedin'] = True
    return redirect('administrador:index')

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

        context={
            # 'all_orders': Order.objects.all()
            #"todasLasOrdenes": ordenes
            "todasLasOrdenes": page,
            }
        return render(request, "master/dashboard_orders.html", context)