from django.shortcuts import render
from apps.productos.models import Producto
from django.db.models import Count
from django.db.models import F
import requests
import json
# aqui se deben importar todos los modelos de las aplicaciones!
#from apps.tienda.models import pagos
#from apps.administrador.models import Producto

# Create your views here.
def index(request):

    # if 'total_spent' not in request.session.keys():
    #     request.session['total_spent'] = 0

    # if 'products_ordered' not in request.session.keys():
    #     request.session['products_ordered'] = 0

    # if 'product_price' not in request.session.keys():
    #     request.session['product_price'] = 0
    
    if 'carrito' not in request.session.keys():
        request.session['carrito'] = {
            "productos" : [],
            "productos_ordenados" : 0,
            "precio_producto" : 0,
            "precio_total" : 0,
        }

    # obetener datos de la tienda:
    productos_request = requests.get("https://fakestoreapi.com/products")
    api = json.loads(productos_request.content)
    descuento = 0.1
    # Victor al registrar un usuario debe obtener un 10% en su primera compra!
    context = {
        "productosApi" : api,
        "productos" : Producto.objects.all(),
        "categorias" : Producto.objects.values('categoria').distinct(),
        "cantidadProdCat" : Producto.objects.all().values('categoria').annotate(cantidadProd=Count("categoria")).order_by('-cantidadProd'),
        "precioPromo": Producto.objects.all().annotate(precio_original=F("precio")*(1.0+descuento)),
        "descuento" : str(int(descuento*100))+"%"
        }
    return render(request, "master/index.html", context)