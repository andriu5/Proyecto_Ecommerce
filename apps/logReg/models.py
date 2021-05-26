from __future__ import unicode_literals
from django.db import models
# from django.db.models.fields import AutoField, CharField, FloatField, IntegerField
# from django.db.models.fields.related import ForeignKey
# from django.contrib.auth.models import User

# # Create your models here.
# class Categorias(models.Model):
#     categoria = CharField(max_length=50, primary_key=True)

# class Products(models.Model):
#     id = AutoField(auto_created=True, primary_key=True)
#     title = CharField(max_length=50)
#     price = FloatField(default=0.0)
#     description = CharField(max_length=250, null=True, default='')
#     image = CharField(max_length=500)
#     categorty = ForeignKey(Categorias, on_delete=models.PROTECT)

# class Carrito(models.Model):
#     id = AutoField(auto_created=True, primary_key=True)

# class CarritoProducto(models.Model):
#     id = AutoField(auto_created=True, primary_key=True)
#     id_cart = ForeignKey(Carrito, on_delete=models.PROTECT)
#     id_product = ForeignKey(Products, on_delete=models.PROTECT)
#     user_id = ForeignKey(User, on_delete=models.PROTECT)