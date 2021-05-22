from django.shortcuts import render
# aqui se deben importar todos los modelos de las aplicaciones!
#from apps.tienda.models import pagos
#from apps.administrador.models import Producto

# Create your views here.
def index(request):
    # Jorge aqui van las llamadas a la base de datos. Ejemplo:
    ##productos = Productos.objects.all()
    ##... = ....objects.all()

    context = {
        ##"productos" : productos,
        ##"..." : ...
        }
    return render(request, "master/index.html", context)