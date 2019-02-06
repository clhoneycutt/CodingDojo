from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from ..books.models import Review
import bcrypt


def index(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    return render(request, 'users/index.html')


def show(request, userid):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
        return render(request, 'users/index.html')


    try:
        user = User.objects.get(id=userid)
        context = {
            'user': user,
            'reviews': user.reviews.all()
        }
        return render(request, 'users/show.html', context)
    except:
        error = "We have encountered a problem while accessing this user. Please contact an administrator."
        messages.error(request, error)
        return redirect('books:index')


def create(request):
    if request.method == 'POST':
        registeringUser = request.POST
        errors = User.objects.regValidate(registeringUser)
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('main:index')
        
        User.objects.createUser(registeringUser)
        createdUser = User.objects.last()
        request.session['loggedIn'] = True
        request.session['userid'] = createdUser.id
        request.session['first_name'] = createdUser.first_name
        
        return redirect('main:success')

    else:
        print('redirecting as GET method')
        return redirect('main:index')


def login(request):
    if request.method == 'POST':
        userInfo = request.POST
        errors = User.objects.loginValidate(userInfo)

        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('main:index')
        else:
            if User.objects.pwcheck(userInfo):
                user = User.objects.get(email=userInfo['emailLogin'])
                request.session['loggedIn'] = True
                request.session['userid'] = user.id
                request.session['first_name'] = user.first_name
                return redirect('main:success')
            else:
                error = "We have encountered a problem logging you in"
                messages.error(request, error)
                return redirect('main:index')
    else:
        return redirect('main:index')


def success(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
        return redirect('main:index')
    if not request.session['loggedIn']:
        return redirect('main:index')

    return render(request, 'users/success.html')


def logout(request):
    if request.session:
        request.session.flush()
    return redirect('main:index')