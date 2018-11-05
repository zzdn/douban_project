from django.shortcuts import render

# Create your views here.
from .models import *
def login(request):
    return render(request,"users/db_login.html")

def register(request):
    return render(request,"users/db_register.html")