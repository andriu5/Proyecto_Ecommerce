from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import NewUserForm, UserForm, EditProfileForm, EditPasswordChangeForm

def home(request):
    return render(request, 'master/index.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:  # si el Usuario Existe!
            # Redirect to a success page.
            login(request, user)
            messages.success(request, ('Usuario ha iniciado sesión correctamente!'))
            return redirect('usuarios:home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('Error en el inicio de sesión!'))
            return redirect('usuarios:login')
    else:
        return render(request, 'master/users_login.html', {})

def logout_user(request):
    logout(request)
    # Redirect to a success page.
    messages.success(request, ('Usted ha cerrado sesión!'))
    return redirect('usuarios:home')

def register_user(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid(): 
            form.save() # Si los Datos ingresados son validos guardamos los datos en la base de datos!
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('Usuario registrado correctamente!'))
            return redirect('usuarios:home')
    else:
        #form = UserCreationForm()
        form = NewUserForm()
        context = {'form': form}
        return render(request, 'master/users_register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        #form = UserChangeForm(request.POST, instance=request.user)
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid(): 
            form.save() # Si los Datos ingresados son validos guardamos los datos en la base de datos!
            messages.success(request, ('Perfil de usuario editado correctamente!'))
            return redirect('usuarios:home')
    else:
        #form = UserChangeForm(instance=request.user)
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, 'master/users_edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        #form = PasswordChangeForm(data=request.POST, user=request.user)
        form = EditPasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid(): 
            form.save() # Si los Datos ingresados son validos guardamos los datos en la base de datos!
            update_session_auth_hash(request, form.user) # para el sistema que no me saque de la sesion!
            messages.success(request, ('Contraseña cambiada correctamente!'))
            return redirect('usuarios:home')
    else:
        form = EditPasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'master/users_change_password.html', context)
