from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    return render(request, 'loginReg/index.html')

def register(request):
    if request.method == 'POST':
        registeringUser = request.POST
        errors = User.objects.regValidate(registeringUser)
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('loginReg:index')
        
        User.objects.createUser(registeringUser)
        request.session['firstName'] = registeringUser['first_name']
        request.session['loggedIn'] = True
        
        return redirect('loginReg:success')

    else:
        print('redirecting as GET method')
        return redirect('loginReg:index')

def login(request):
    if request.method == 'POST':
        loginAttemptInfo = request.POST
        errors = User.objects.loginValidate(loginAttemptInfo)

        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('loginReg:index')
        else:
            if User.objects.attemptLogin(loginAttemptInfo):
                user = User.objects.get(email=loginAttemptInfo['emailLogin'])
                request.session['loggedIn'] = True
                request.session['userid'] = user.id
                return redirect('loginReg:success')
            else:
                error = "We have encountered a problem"
                messages.error(request, error)
                return redirect('loginReg:index')
    else:
        return redirect('loginReg:index')

def success(request):
    return render(request, 'loginReg/success.html')

def logout(request):
    request.session.flush()
    return redirect('loginReg:index')