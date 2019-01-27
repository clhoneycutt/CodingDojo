from django.shortcuts import render, redirect

def index(request):
    return render(request, 'loginReg/index.html')

def register(request):
    return redirect('loginReg:index')

def login(request):
    return redirect('loginReg:index')