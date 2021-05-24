from django.shortcuts import render, redirect
from django.contrib import messages
from apps.logReg.models import User
import bcrypt
from django.core.paginator import EmptyPage, Paginator

productos = [
    {
        "id":1,
        "nombre" : "Computador Portatíl",
        "cantidad_inventario" : 100,
        "cantidad_vendido" : 1,
        "imagen" : {"url":"/media/notebook_hp_14_cf2051la_intel_CoreI3_4gb_Ram.jpg"},
    },
    {
        "id":2,
        "nombre" : "Jeans Mujer",
        "cantidad_inventario" : 100,
        "cantidad_vendido" : 99,
        "imagen" : {"url":"/media/jeans_mujer.jpg"},
    },
    {
        "id":3,
        "nombre" : "Pantalon Trekking",
        "cantidad_inventario" : 100,
        "cantidad_vendido" : 85,
        "imagen" : {"url":"/media/pantalon_trekking.jpg"},
    },
    {
        "id":4,
        "nombre" : "Pantalon Trekking Kaki",
        "cantidad_inventario" : 100,
        "cantidad_vendido" : 85,
        "imagen" : {"url":"/media/pantalon_kaki-2.jpg"},
    },
    {
        "id":5,
        "nombre" : "Polera Seleccion Chilena 2019",
        "cantidad_inventario" : 1000,
        "cantidad_vendido" : 850,
        "imagen" : {"url":"/media/SELEC.-CHILENA-2019.jpg"},
    },
    {
        "id":6,
        "nombre" : "Polera cuello redondo Naranja",
        "cantidad_inventario" : 1000,
        "cantidad_vendido" : 850,
        "imagen" : {"url":"/media/polera-cuello-redondo-naranja.jpg"},
    },
    {
        "id":7,
        "nombre" : "Computador Portatíl",
        "cantidad_inventario" : 100,
        "cantidad_vendido" : 1,
        "imagen" : {"url":"/media/notebook_hp_14_cf2051la_intel_CoreI3_4gb_Ram.jpg"},
    },
    {
        "id":8,
        "nombre" : "Jeans Mujer",
        "cantidad_inventario" : 100,
        "cantidad_vendido" : 99,
        "imagen" : {"url":"/media/jeans_mujer.jpg"},
    },
    {
        "id":9,
        "nombre" : "Pantalon Trekking",
        "cantidad_inventario" : 100,
        "cantidad_vendido" : 85,
        "imagen" : {"url":"/media/pantalon_trekking.jpg"},
    },
    {
        "id":10,
        "nombre" : "Pantalon Trekking Kaki",
        "cantidad_inventario" : 100,
        "cantidad_vendido" : 85,
        "imagen" : {"url":"/media/pantalon_kaki-2.jpg"},
    },
    {
        "id":11,
        "nombre" : "Polera Seleccion Chilena 2019",
        "cantidad_inventario" : 1000,
        "cantidad_vendido" : 850,
        "imagen" : {"url":"/media/SELEC.-CHILENA-2019.jpg"},
    },
    {
        "id":12,
        "nombre" : "Polera cuello redondo Naranja",
        "cantidad_inventario" : 1000,
        "cantidad_vendido" : 850,
        "imagen" : {"url":"/media/polera-cuello-redondo-naranja.jpg"},
    },
]

# Create your views here.
def index(request):
    if request.method == "GET":
        # Paginamos el dashboard de Productos cada 4 elementos usando Paginator
        p = Paginator(productos, 4)
        page_num = request.GET.get('/productos/dashboard/<int:page>/', 1)
        page = p.page(page_num) # página desde donde comenzamos a mostrar, ósea, si colocamos 2 entregara el id=5 e id=6
        context = {
            # "todosLosProductos" : productos,
            "todosLosProductos" : page,
            "cats": ["Pantalones", "Poleras", "Cocina", "Frutas", "Verduras", "Zapatos", "Zapatillas", "Celulares", "Computacion", "Juegos de Video", "Libros"]
        }
        return render(request, "master/listar_productos.html", context)

def dashboard(request, page):
    #tener cuidado con la seguridad de la pagina!
    if 'admin_loggedin' in request.session and request.session['admin_loggedin'] == True:
        # Paginamos el dashboard de Ordenes cada 4 elementos usando Paginator
        p = Paginator(productos, 4)
        page_num = request.GET.get('dashboard/orders/<int:page>/',page)

        print("\nNúmero de páginas en el Dashboard de administración de Ordenes:", p.num_pages,"\n")

        
        # Si el administrador trata de ir a una página que no existe. ¡Lo forzamos a ir a la página 1!
        try:
            page = p.page(page_num) # página desde donde comenzamos a mostrar, ósea, si colocamos 2 entregara el id=5 e id=6
        except EmptyPage:
            page = p.page(1)

        context={
            # 'todosLosProductos': Productos.objects.all()
            # "todosLosProductos" : productos,
            "todosLosProductos": page,
            }
        return render(request, "master/listar_productos.html", context)

def admin_productos(request):
    if 'admin_loggedin' in request.session and request.session['admin_loggedin'] == True:
        pass
    request.session.clear()
    request.session['admin_bad_loggedin'] = True
    return redirect('administrador:index')

def add_producto(request):
    print('*'*100)
    print('Agregando un nuevo Producto...')
    pass

def edit_producto(request, id):
    print('*'*100)
    print(f'Editando Producto ID: {id}...')
    pass
def update_producto(request, id):
    print('*'*100)
    print(f'Actualizando Producto ID: {id}...')
    pass

def delete_producto(request):
    pass