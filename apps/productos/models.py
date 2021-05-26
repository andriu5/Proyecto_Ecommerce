from __future__ import unicode_literals
from django.db import models
# from apps.logReg.models import User
from django.contrib.auth.models import User

class ProductoManager(models.Manager):
    def product_validation(self, postData):
        errores = {}
        try:
            postdata_name = postData['nombre']
            print("Imprimiendo desde product_validation: ", postdata_name.isalpha())
            print("Imprimiendo desde product_validation: ", postdata_name)
            if len(postdata_name) < 2 or not postdata_name.isalpha():
                errores['nombre_prod'] = "Error: El nombre del producto debe ser de al menos 2 caracteres."
        except Exception as e:
            print(e)
            errores['nombre_prod'] = "Error: El nombre del producto debe ser de al menos 2 caracteres."
        print("Imprimiendo desde product_validation: ",postData['descripcion'])
        print(postData['descripcion'])
        if len(postData['descripcion']) < 10 or not postData['descripcion'].isalpha():
            errores['descripcion'] = "Error: La descripción del producto debe ser de al menos 10 caracteres."
        try:
            if int(postData['precio']) < 0 and not postData['precio'].isalpha():
                errores['precio_negativo'] = "Error: El precio ingresado del producto debe ser un número mayor a cero."
        except Exception as e:
            errores['precio_negativo'] = "Error: El precio ingresado del producto debe ser un número mayor a cero."
        if len(postData['categoria']) < 2 or not postData['categoria'].isalpha():
            errores['categoria_corta'] = "Error: El nombre de la categoría debe ser de al menos 2 caracteres."
        # validar si la imagen fue ingresada en la base datos!
        return errores

    def category_num(self, cat):
        return self.filter(category=cat).count()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_vendida=models.PositiveIntegerField(default=0)
    precio=models.PositiveIntegerField(default=0)
    categoria=models.CharField(max_length=255)
    inventario=models.PositiveIntegerField(default=0)
    descripcion=models.TextField()
    imagen = models.ImageField(upload_to='productos', null=True)
    uploaded_by = models.ForeignKey(User, related_name="producto_uploaded", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = ProductoManager()
    def __str__(self):
        return self.nombre
