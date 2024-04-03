from django.shortcuts import render
from .models import Empresa

def inicio(request):
    return render(request,'inicio.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def personuser(request):
    return render(request,'personuser.html')