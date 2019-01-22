from django.shortcuts import render, redirect
from apps.users.models import *



def new(request): # GET Method
    return render(request, 'users/create.html')

def create(request): # POST Method
    return redirect('/users')

def show(request): # GET Method
    return render(request, 'users/show.html')

def edit(request): # GET Method
    return render(request, 'users/edit.html')

def update(request): # POST Method
    return redirect('/users')

def destroy(request): # GET Method
    return redirect('/users')

def index(request): # GET Method
    return render(request, 'users/index.html')
