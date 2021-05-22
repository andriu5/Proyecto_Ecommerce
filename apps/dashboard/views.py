from django.shortcuts import render
from apps.logReg.models import User

# Create your views here.
def admin_dashboard(request):
    if request.method == "GET":
        context={
        }
        return render(request, "master/dashboard_orders.html", context)