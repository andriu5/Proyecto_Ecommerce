from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def reg_validaton(self, postData):
        
        print(postData)
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData['email']):    # probar si un campo coincide con el patrón
            errors['email'] = "Error: Invalid email address!"
        if len(postData['first_name']) == 0 or not postData['first_name'].isalpha():
            errors['first_name_blank'] = "Error: Please Enter a Valid First Name"
        if len(postData['last_name']) == 0 or not postData['last_name'].isalpha():
            errors['last_name_blank'] = 'Error: Please Enter a Valid Last Name'
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors['first_name_short'] = "Error: First Name should be at least 2 characters"
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors['last_name_short'] = "Error: Last Name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Error: Password should be at least 8 characters"
        if postData['password'] != postData['confirmPassword']:
            errors['password'] = "Error: The Passwords does not match!"
        return errors
   
    def log_validation(self, postData):
        errors = {}
        try:
            user = User.objects.get(email = postData['email'])
        except:
            errors['email'] = f"Email address {postData['email']} is not registered in our database!"
            return errors
        if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            errors['password'] = "Password does not match our database!"
        return errors

class User(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    def __repr__(self):
        return f"<User object: ID: {self.id} | Name: {self.nombre} {self.apellido} | Email: {self.email} >"