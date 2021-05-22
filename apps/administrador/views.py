from django.shortcuts import render, redirect
from django.contrib import messages
from apps.logReg.models import User
import bcrypt
from time import gmtime, strftime, time, localtime
from datetime import datetime
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "admin/base.html")