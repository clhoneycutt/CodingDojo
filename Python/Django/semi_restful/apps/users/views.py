from django.shortcuts import render, redirect
from django.contrib import messages
from apps.users.models import *



def index(request): # GET Method
    context = {
        'users': User.objects.all(),
    }

    return render(request, 'users/index.html', context)

def new(request): # GET Method
    return render(request, 'users/create.html')

def show(request, id): # GET Method
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'users/show.html', context)

def edit(request, id): # GET Method
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'users/edit.html', context)

def create(request): # POST Method
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/users/new')
    else:    
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])

        return redirect('/users')

def update(request, id): # POST Method
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect(f'/users/{id}/edit')
    else:
        user = User.objects.get(id=id)
        userDict = request.POST
        user.first_name = userDict['first_name']
        user.last_name = userDict['last_name']
        user.email = userDict['email']
        user.save()
        return redirect(f'/users/{id}/show')

def destroy(request, id): # GET Method
    annihalation = User.objects.get(id=id)
    annihalation.delete()
    return redirect('/users')
