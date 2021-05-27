from .models import Orden

# si no tenemos el orden id lo agregamos a nuestra sesion!
def get_or_set_order_session(request):
    orden_id = request.session.get('order_id', None)
    if orden_id is None:
        orden = Orden()
        orden.save()
        request.session['orden_id'] = orden.id
    else:
        #en caso contrario solo queda ver que no hayan pagado la orden!
        try:
            orden = Orden.objects.get(id=orden_id, ordenado=False)
        except Orden.DoesNotExist:
            #si la orden no existe la creamos!
            orden = Orden()
            orden.save()
            request.session['orden_id'] = orden.id
    
    if request.user.is_authenticated and orden.user is None:
        orden.user = request.user
        orden.save()
    return orden