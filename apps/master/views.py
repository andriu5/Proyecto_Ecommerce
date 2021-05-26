from django.shortcuts import render
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
    context = {
        "productos" : api,
        ##"..." : ...
        }
    return render(request, "master/index.html", context)