from __future__ import unicode_literals
from django.db import models
# from apps.logReg.models import User
from django.contrib.auth.models import User

class ProductoManager(models.Manager):
    def product_validation(self, postData):
        errores = {}
        if len(postData['nombre']) < 2 or not postData['nombre'][0].isalpha():
            errores['nombre_prod'] = "Error: El nombre del producto debe ser de al menos 2 caracteres."
        if len(postData['descripcion']) < 10 or not postData['descripcion'][0].isalpha():
            errores['descripcion'] = "Error: La descripción del producto debe ser de al menos 10 caracteres."
        if float(postData['precio']) < 0:
            errores['precio_negativo'] = "Error: El precio ingresado del producto debe ser un número mayor a cero."
        if len(postData['categoria']) < 2 or not postData['categoria'][0].isalpha():
            errores['categoria_corta'] = "Error: El nombre de la categoría debe ser de al menos 2 caracteres."
        # validar si la imagen fue ingresada en la base datos!
        return errores

    def category_num(self, cat):
        return self.filter(category=cat).count()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_vendida=models.PositiveIntegerField(default=0)
    precio=models.PositiveIntegerField(default=0)
    categoria=models.CharField(max_length=50)
    inventario=models.PositiveIntegerField(default=0)
    descripcion=models.TextField()
    imagen = models.ImageField(upload_to='media', default='none.jpg')
    uploaded_by = models.ForeignKey(User, related_name="producto_uploaded", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = ProductoManager()
    def __str__(self):
        return self.nombre
