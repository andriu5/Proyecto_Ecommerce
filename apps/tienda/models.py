from django.db import models
from apps.productos.models import Producto
from django.contrib.auth.models import User


class Direccion(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Biling'),
        ('S', 'Shipping')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion1 = models.CharField(max_length=150)
    direccion2 = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=150)
    codigo_postal = models.CharField(max_length=150)
    tipo_de_direccion = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False) # para que los usuarios puedan selecionar un default address y no tengan que agregar uno nuevo a cada rato!

    def __str__(self):
        return f"{self.direccion1}, {self.direccion2}, {self.ciudad}, {self.codigo_postal}"
    
    #para tener el indice correcto cuando buscamos por amabas ADDRESS_CHOICES!
    class Meta:
        verbose_name_plural = "Addresses"

# class ColourVariation(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class SizeVariation(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

class Orden(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    fecha_compra = models.DateTimeField(blank=True, null=True)
    ordenado = models.BooleanField(default=False)

    billing_address = models.ForeignKey(Direccion, related_name="billing_address", blank=True, null=True, on_delete=models.SET_NULL) #si borramos una direccion no queremos perderla!
    shipping_address = models.ForeignKey(Direccion, related_name="shipping_address", blank=True, null=True, on_delete=models.SET_NULL) #si borramos una direccion no queremos perderla!

    def __str__(self):
        return self.numero_de_referencia
    
    #Este es el numero que le damos a un cliente cuando se tiene que hacer una referencia a una orden!
    @property
    def numero_de_referencia(self):
        return f"ORDEN-{self.pk}"


class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Pagos(models.Model):
    orden = models.ForeignKey(Orden, related_name='pagos', on_delete=models.CASCADE) #queremos obtener todos las ordenes asociadas a este Pago!
    metodo_de_pago = models.CharField(max_length=20, choices=(
        ('Credito', 'Credito'),
        ('Debito', 'Debito'),
        ('Paypal', 'Paypal'),
    ))
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    total = models.FloatField()
    respuesta = models.TextField() # aqui guardamos la respuesta HTTP de las API de las tarjeta de credito y debito

    @property
    def numero_de_referencia(self):
        return f"PAGO-{self.orden}-{self.pk}"

