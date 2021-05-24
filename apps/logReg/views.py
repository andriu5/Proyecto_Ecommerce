from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'logReg/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")    

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'logReg/login.html',{"error":True})  
    else:
        return render(request, 'logReg/login.html', {})  

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successfully")
            return HttpResponseRedirect(reverse('index'))
        messages.error(request,"UnsuccessFully Registration. Invalid information.")
    form = NewUserForm()
    return render(request,'logReg/sign_up.html',{'register_form':form})