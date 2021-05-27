from django.shortcuts import render, redirect
from django.contrib import messages
#from apps.logReg.models import User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from .models import Producto, Orden, OrdenItem
from .models import Producto
from .forms import  formProducto
import bcrypt
from django.core.paginator import EmptyPage, Paginator
from django.core.files.storage import FileSystemStorage

# Create your views here.
@login_required
def index(request):
    if request.method == "GET":
        # Paginamos el dashboard de Productos cada 4 elementos usando Paginator
        productos = Producto.objects.all()
        p = Paginator(productos, 4)
        page_num = request.GET.get('/productos/dashboard/<int:page>/', 1)
        page = p.page(page_num) # página desde donde comenzamos a mostrar, ósea, si colocamos 2 entregara el id=5 e id=6
        currentUserID = request.session['admin']['id']
        context = {
            # "todosLosProductos" : productos,
            "todosLosProductos" : page,
            "cats": ["Pantalones", "Poleras", "Cocina", "Frutas", "Verduras", "Zapatos", "Zapatillas", "Celulares", "Computacion", "Juegos de Video", "Libros"],
            "user": request.user,
        }
        return render(request, "master/listar_productos.html", context)

@login_required
def dashboard(request, page):
    #tener cuidado con la seguridad de la pagina!
    if 'admin_loggedin' in request.session and request.session['admin_loggedin'] == True:
        # Paginamos el dashboard de Ordenes cada 4 elementos usando Paginator
        productos = Producto.objects.all()
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

@login_required
def admin_productos(request):
    if 'admin_loggedin' in request.session and request.session['admin_loggedin'] == True:
        context = {
            #"cats": ["Pantalones", "Poleras", "Cocina", "Frutas", "Verduras", "Zapatos", "Zapatillas", "Celulares", "Computacion", "Juegos de Video", "Libros"]
            "productos": Producto.objects.all()
        }
        return render(request, "master/add_productos.html", context)
    request.session.clear()
    request.session['admin_bad_loggedin'] = True
    return redirect('administrador:index')

@login_required
def add_producto(request):
    print('*'*100)
    print('Agregando un nuevo Producto...')
    if 'admin' in request.session.keys():
        #Validamos el formulario contra la base de datos
        print(request.POST)
        errors = Producto.objects.product_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('productos:admin_productos')
        else:
            # #Validamos si la imagen del producto esta en la base de datos!
            # if Producto.objects.filter(imagen=request.FILES['imagen']).exists():
            #     messages.add_message(request, messages.ERROR, f"Error: La imagen '{request.POST['imagen']}' no puede agregarse por que ya existe esa imagen en la base de datos!")
            #     return redirect('productos:admin_productos')
            # else:
            if request.method == "POST":
                nuevo_producto = Producto.objects.create(
                    nombre = request.POST['nombre'],
                    precio = int(request.POST['precio']),
                    categoria = request.POST['categoria'],
                    inventario = int(request.POST['inventario']),
                    descripcion = request.POST['descripcion'],
                    imagen = request.FILES['imagen'],
                    uploaded_by = request.user
                    )
                print(f"Info: Nuevo Producto Agregado a la base de datos!\n")
                return redirect('productos:index')
            return redirect('administrador:index')

@login_required
def edit_producto(request, id):
    print('*'*100)
    print(f'Editando Producto ID: {id}...')
    context = {
        "user": request.user,
        "producto": Producto.objects.get(id=id),
    }
    return render(request, "master/edit_productos.html", context)

@login_required
def update_producto(request, id):
    print('*'*100)
    print(f'Actualizando Producto ID: {id}...')
    esteProducto = Producto.objects.get(id=id)
    if 'admin' in request.session.keys():
        #TODO: Validamos el formulario contra la base de datos
        print(request.POST)
        errors = Producto.objects.product_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/productos/{id}/')
        else:
            if request.method == "POST":
                if request.POST['nombre']:
                    esteProducto.nombre = request.POST['nombre']
                if request.POST['precio']:
                    esteProducto.precio = int(request.POST['precio'])
                if request.POST['categoria']:
                    esteProducto.categoria = request.POST['categoria']
                if request.POST['inventario']:
                    esteProducto.inventario = int(request.POST['inventario'])
                if request.POST['descripcion']:
                    esteProducto.descripcion = request.POST['descripcion']
                if request.FILES['imagen']:
                    esteProducto.imagen = request.FILES['imagen']
                esteProducto.uploaded_by = request.user
                esteProducto.save()
                print(f"Info: Producto correctamente editado en la base de datos!\n")
                return redirect('productos:index')
            return redirect('administrador:index')

@login_required
def delete_producto(request,id):
    print('*'*100)
    print(f'Removiendo producto ID: {id}...')
    deleteThisProducto = Producto.objects.get(id=id)
    if request.user.is_authenticated:
        deleteThisProducto.delete()
        return redirect('productos:index')
    else:
        return redirect('administrador:index')

@login_required
def info_producto(request,id):
    print('*'*100)
    print(f'Información producto ID: {id}...')
    context = {
        "producto" : Producto.objects.get(id=id),
    }
    return render(request, "master/ficha_producto.html", context)