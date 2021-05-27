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
    # Jorge aqui van las llamadas a la base de datos. Ejemplo:
    ##productos = Productos.objects.all()
    ##... = ....objects.all()

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