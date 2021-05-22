from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from django.core.validators import MinValueValidator, MaxValueValidator

class UserManager(models.Manager):
    def reg_validaton(self, postData):
        
        print(postData)
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):    # probar si un campo coincide con el patrón
            errors['email'] = "Error: dirección de email invalido!"
        if len(postData['nombre']) == 0 or not postData['nombre'].isalpha():
            errors['first_name_blank'] = "Error: Por favor ingrese un Nombre valido"
        if len(postData['apellido']) == 0 or not postData['apellido'].isalpha():
            errors['last_name_blank'] = 'Error: Por favor ingrese un Apellido valido.'
        if len(postData['nombre']) < 2 or not postData['nombre'].isalpha():
            errors['first_name_short'] = "Error: el campo Nombre debe tener al menos 2 caracteres."
        if len(postData['apellido']) < 2 or not postData['apellido'].isalpha():
            errors['last_name_short'] = "Error: el Apellido debe tener al menos 2 caracteres"
        if len(postData['password']) < 8:
            errors['password'] = "Error: El Password debe tener al menos 8 caracteres"
        if postData['password'] != postData['confirmPassword']:
            errors['password'] = "Error: ¡Las contraseñas ingresadas no coinciden!"
        return errors
   
    def log_validation(self, postData):
        errors = {}
        try:
            user = User.objects.get(email = postData['email'])
        except:
            errors['email'] = f"Dirección de Email {postData['email']} no esta registrado en la base de datos!"
            return errors
        if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            errors['password'] = "Password no coincide con la base de datos!"
        return errors

class User(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    nivel_usuario = models.PositiveIntegerField(validators= [
        MinValueValidator(1, message = "El código de Usuario debe ser igual a 1 para clientes."), 
        MaxValueValidator(2, message = "El código de Usuario debe ser igual a 2 para administradores."),
        ]) # Area de trabajo del Usuario - 1 a 5
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    def __repr__(self):
        return f"<User object: ID: {self.id} | Name: {self.nombre} {self.apellido} | Email: {self.email} >"