from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
from time import gmtime, strftime, time, localtime
from datetime import datetime
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "login_registration/index.html")

def register(request):
    if request.POST['logReg'] == 'register':
        errors = User.objects.reg_validaton(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('usuarios:index')
    else:
        if request.method == "POST":
            #Verificar Email!
            if User.objects.filter(email=request.POST['email']).exists():
                messages.add_message(request, messages.ERROR, f"Error: email '{request.POST['email']}' is already taken!")
                return redirect('usuarios:index')
            else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash

                new_user = User.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'], nivel_usuario=1, email=request.POST['email'], password=pw_hash)
                print(f"Info: Nuevo cliente agregado a la base de datos.\n Nombre: {new_user.nombre} {new_user.apellido} | Email: {new_user.email}")
                #messages.success(request,"Successfully registered!")
                request.session['user'] = {
                    'id': new_user.id,
                    'name': new_user.nombre,
                    'lastname': new_user.apellido
                    }
                return redirect("usuarios:success") # nunca renderizar en una publicación, ¡siempre redirigir!

def success(request):
    if request.method == "GET":
        if 'user' not in request.session.keys():
            print('redirecting hacker for login...')
            # messages.add_message(request, messages.ERROR, f"Error: Please login to the App!")
            return redirect('usuarios:index')
        else:
            return render(request, "login_registration/success.html")

def login(request):
    if request.POST['logReg'] == 'login':
        errors = User.objects.log_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('usuarios:index')
        else:
            # ver si el nombre de usuario proporcionado existe en la base de datos
            user = User.objects.filter(email=request.POST['email']) # ¿Por qué usamos el filtro aquí en lugar de get?
            if user: # tenga en cuenta que aquí aprovechamos la veracidad: una lista vacía devolverá falso
                logged_user = user[0] 
                user = User.objects.get(email = request.POST['email'])
                request.session['user'] = {
                    'id': user.id,
                    'name': user.nombre,
                    'lastname': user.apellido
                }
                # asumiendo tenemos un usuario con este nombre de usuario, éste sería el primero en la lista que obtenemos
                # por supuesto, deberíamos tener cierta lógica para evitar duplicados de nombres cuando creamos usuarios
                # usa el método check_password_hash de bcrypt, pasando el hash de nuestra base de datos y la contraseña del formulario
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                # si obtenemos True después de validar la contraseña, podemos poner la identificación del usuario en la sesión
                    request.session['user_id'] = logged_user.id
                    # ¡Nunca renderices en una publicación, siempre redirigir!
                    #messages.success(request,"Successfully logged in!")
                    return redirect('quotes_app:dashboard')
            # si no encontramos nada en la base de datos buscando por nombre de usuario o si las contraseñas no coinciden, 
            # redirigir a una ruta segura
            return redirect('usuarios:index')

def logout(request):
    for key in request.session.keys(): # Imprimimos todas las claves de la session antes de borrar
        print("session key: ",key)
        print("session key type(): ",type(key))
    request.session.clear() # borramos todas las claves de la session
    return redirect("usuarios:index") # go to root: "/"

def verificar_email(request):
    if request.method == "POST":
        email = request.POST['email']
        print("Email:", email)
        if User.objects.filter(email=request.POST['email']).exists():
            # Valimos que no exista 
            # Guardamos los datos en la base de datos
            print("Imprimiendo desde Verificar Email!")
            # return HttpResponse( f"Error: email '{email}' is already in the data base!")\
            return JsonResponse({"errors":  f"Error: email '{email}' is already in the data base!"})