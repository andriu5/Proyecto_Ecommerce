import datetime
import json
from django.views import generic
from .utils import get_or_set_order_session
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from apps.productos.models import Producto
from apps.productos.forms import  formProducto
from .models import Orden, OrdenProducto, Direccion, Pagos
from .forms import ShippingAddressForm, AddToCartForm
from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.db.models import Sum


def show_producto(request, id):
    print('*'*100)
    print(f'Mostrando Producto ID: {id}...')
    producto = Producto.objects.get(id=id)
    form = AddToCartForm()
    context = {
        'form': form,
        "producto": producto,
        "productos_similares": Producto.objects.filter(categoria=producto.categoria).exclude(id=producto.id)
    }
    return render(request, "master/show_productos.html", context)


def carrito_productos(request):
    #TODO: agregar codigo de cuando el Usuario esta registrado en la tienda!
    if request.method == "GET":
        form = AddToCartForm()
        context = {
            'form': form,
            "productos": Producto.objects.all(),
            "total" : Producto.objects.aggregate(Sum('precio')), #¡Esto es solopara probar! se debe reemplazar por el valor de la session!
        }
        
        return render(request, "master/carrito.html", context)

def agregar_a_carrito(request):
    if request.method == "POST":
        if request.POST['producto-carrito'] == 'producto-detalle':
            producto_id = request.POST['producto_id']
            #Guardamos lo que sea que el usuario haya Posteado en form!
            form = AddToCartForm(request.POST or None)
            #Validamos el formulario:  Si los datos son validos guardamos en la sesion de compra!
            if form.is_valid():
                #tenemos 2 casos: usuarios logeados y usuarios no logeados en la aplicacion. Los trabajamos por separado
                
                #Para usuarios logeados:
                if request.user is not None:
                    request.user = {
                            'id': request.user.id,
                            'cantidad': request.user.first_name,
                            'productos': ""
                        }
                else:
                    request.session['carrito'] = 1
                    request.session['producto_id'] = producto_id
        return redirect("tienda:show_prod", producto_id)

#Esto lo saque de las tareas Antiguas: Amadon!
def post_checkout(request):
    #TODO: agregar codigo de cuando el Usuario esta registrado en la tienda!
    if request.method == "POST":
        id_from_form = request.POST['product_id']
        print("Product ID:", request.POST['product_id'])

        quantity_from_form = int(request.POST["quantity"])
        #price_from_form = float(request.POST["price"])
        
        #Conclusion: El precio siempre tiene que estar en el lado del Back-End y al usuario se le envian IDs que no siginifcan nada para él!
        price_from_form = Producto.objects.get(id=id_from_form).price
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        #new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        
        #En la página de pago, calcula y muestra el cargo total del pedido más reciente
        request.session['product_price'] = float("{:.2f}".format(quantity_from_form * price_from_form))
        
        #En la página de pago, calcula y muestra la cantidad total de todos los pedidos combinados
        request.session['products_ordered'] += quantity_from_form

        #En la página de pago, calcula y muestra el monto total cobrado por todos los pedidos combinados
        request.session['total_spent'] += float("{:.2f}".format(quantity_from_form * price_from_form))

        return redirect("tienda:confirmacion_compra")

def confirmacion_compra(request):
    #TODO: agregar codigo de cuando el Usuario esta registrado en la tienda!
    if request.method == "GET":
        context = {
        }
        return render(request, "master/confirmacion_compra.html", context)

def reset(request):
    #TODO: se resetea la sesion del usuario que compro algo en la tienda!
    for key in request.session.keys(): # Imprimimos todas las claves de la session antes de borrar
        print("session key: ",key)
        print("session key type(): ",type(key))
    request.session.clear() # borramos todas las claves de la session
    return redirect("/")

# class CartView(generic.TemplateView):
#     template_name = 'master/carrito.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(CartView, self).get_context_data(**kwargs)
#         context["orden"] = get_or_set_order_session(self.request)
#         return context