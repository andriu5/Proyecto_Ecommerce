import datetime
import ast
import json
from django.views import generic
from .utils import get_or_set_order_session
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from apps.productos.models import Producto
from apps.productos.forms import  formProducto
from .models import Orden, OrdenProducto, Direccion, Pagos
from .forms import AddressForm, AddToCartForm
from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from django.db.models import Sum


def show_producto(request, id):
    print('*'*100)
    print(f'Mostrando Producto ID: {id}...')
    producto = Producto.objects.get(id=id)
    p = Producto.objects.get_producto(producto)
    print(f'Mostrando Producto desde show_producto: {producto}')
    print(f'Mostrando p desde show_producto: {p}')

    form = AddToCartForm()
    context = {
        'form': form,
        "producto": producto,
        "p": p,
        "productos_similares": Producto.objects.filter(categoria=producto.categoria).exclude(id=producto.id)
    }
    return render(request, "master/show_productos.html", context)


def carrito_productos(request):
    #TODO: agregar codigo de cuando el Usuario esta registrado en la tienda!
    if request.method == "GET":
        if request.user is not None:
            form = AddressForm()
            context = {
                'form': form,
                "productos": Producto.objects.all(),
                "total" : Producto.objects.aggregate(Sum('precio')), #¡Esto es solopara probar! se debe reemplazar por el valor de la session!
            }
            return render(request, "master/carrito.html", context)
        else:
            context = {
                "productos": Producto.objects.all(),
                "total" : Producto.objects.aggregate(Sum('precio')), #¡Esto es solo para probar! se debe reemplazar por el valor de la session!
            }
            return render(request, "master/carrito.html", context)


def agregar_a_carrito(request):
    print('*'*100)
    print('Agregando Producto con ID: ',request.POST['producto_id'],' al Carrito...')
    if request.method == "POST":
        producto_id = request.POST['producto_id']
        producto = Producto.objects.get(id=producto_id)
        p = Producto.objects.get_producto(producto)
        # ast to solve single quote and final comma issues
        producto_ast = ast.literal_eval(p)
        producto_carrito = json.dumps(producto_ast)
        print(producto_carrito)
        cart_list = list(request.session['carrito']['productos'])
        cart_list.append(producto_ast)
        request.session['carrito']['productos'] = cart_list
        print("Product ID:", request.POST['producto_id'])
        print("Carrito:", request.session['carrito']['productos'])

        quantity_from_form = int(request.POST["cantidad"])
        price_from_form = int(Producto.objects.get(id=producto_id).precio)
        print("Precio Producto: ",price_from_form)
        total_charge = quantity_from_form * price_from_form
        print("Total de productos añadidos: ", total_charge)
        #En la página de pago, calcula y muestra el cargo total del pedido más reciente
        request.session['carrito']['precio_producto'] = quantity_from_form * price_from_form
        
        #En la página de pago, calcula y muestra la cantidad total de todos los pedidos combinados
        request.session['carrito']['productos_ordenados'] += quantity_from_form
        print("Productos Ordenados: ",request.session['carrito']['productos_ordenados'])

        #En la página de pago, calcula y muestra el monto total cobrado por todos los pedidos combinados
        request.session['carrito']['precio_total'] += int(quantity_from_form * price_from_form)
        print("Precio Total: ",request.session['carrito']['precio_total'] )

        # si no hago 'request.session.modified', no se guardan los valores anidados en el carrito. Ver: https://docs.djangoproject.com/en/2.2/topics/http/sessions/#when-sessions-are-saved
        request.session.modified = True

        return redirect("tienda:show_prod", producto_id)

def carrito_debug(request):
    return JsonResponse({"carrito": request.session['carrito']})

#Esto lo saque de las tareas Antiguas: Amadon!
def post_checkout(request):
    #TODO: agregar codigo de cuando el Usuario esta registrado en la tienda!
    if request.method == "POST":
        form = AddressForm(request.POST or None)
        #if form.is_valid():
            #form.save()
        return render(request, 'master/confirmacion_compra.html')
            # id_from_form = request.POST['product_id']
            # print("Product ID:", request.POST['product_id'])

            # quantity_from_form = int(request.POST["quantity"])
            # #price_from_form = float(request.POST["price"])
            
            # #Conclusion: El precio siempre tiene que estar en el lado del Back-End y al usuario se le envian IDs que no siginifcan nada para él!
            # price_from_form = Producto.objects.get(id=id_from_form).price
            # total_charge = quantity_from_form * price_from_form
            # print("Charging credit card...")
            # #new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
            
            # #En la página de pago, calcula y muestra el cargo total del pedido más reciente
            # request.session['product_price'] = float("{:.2f}".format(quantity_from_form * price_from_form))
            
            # #En la página de pago, calcula y muestra la cantidad total de todos los pedidos combinados
            # request.session['products_ordered'] += quantity_from_form

            # #En la página de pago, calcula y muestra el monto total cobrado por todos los pedidos combinados
            # request.session['total_spent'] += float("{:.2f}".format(quantity_from_form * price_from_form))

            # return redirect("tienda:confirmacion_compra")

def confirmacion_compra(request):
    #TODO: agregar codigo de cuando el Usuario esta registrado en la tienda!
    if request.method == "GET":
        context = {
        }
        return render(request, "master/confirmacion_compra.html", context)

# esto no funciona se debe eliminar el Objeto de javascript que esta cargado en el navegador (si uno escribe productos en la consola del nevegador se imprimen todo el contenido de productos que estan cargados en memoria)
def reset(request): 
    logout(request)
    # Redirect to a success page.
    request.session.clear() # borramos todas las claves de la session (La vieja confiable!)
    messages.success(request, ('¡Sesión cerrada - carrito elminado!')) 
    return redirect('/')

def borrar_del_carrito(request,id):
    print('*'*100)
    print(f'Mostrando Producto ID desde vista borrar_del_carrito: {id}...')
    if request.method == "POST":
        producto_a_remover_del_carrito = Producto.objects.get(id=id)
        print(f"El ID del producto {producto_a_remover_del_carrito} que se va sacar del carrito es:", id)
        for item in request.session.items():
            print(item)
        # for key in request.session.keys(): # Imprimimos todas las claves de la session antes de borrar
        #     print("session key: ",key)
        #     print("session key type(): ",type(key))
        # request.session.clear() # borramos todas las claves de la session
        print('*'*100)
        return JsonResponse({"message":  f"El producto '{producto_a_remover_del_carrito.nombre}' fue removido del carrito!"})