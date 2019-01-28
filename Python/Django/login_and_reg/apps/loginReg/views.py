from django.shortcuts import render, redirect
from django.contrib import messages
from apps.loginReg.models import *

def index(request):
    return render(request, 'loginReg/index.html')

def register(request):
    if request.method == 'POST':
        registeringUser = request.POST
        errors = User.objects.regValidate(registeringUser)
        
        if errors:
            for error in errors:
                messages.error(request, error)

            return redirect('loginReg:index')
        else:
            password = registeringUser['passwordReg']
            pwhash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(
                first_name=registeringUser['first_name'],
                last_name=registeringUser['last_name'],
                email=registeringUser['emailReg'],
                pwhash=pwhash
            )

    else:
        return redirect('loginReg:index')

def login(request):
    return redirect('loginReg:index')