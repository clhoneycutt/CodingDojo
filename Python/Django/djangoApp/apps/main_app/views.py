from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(req):
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)

def new(req):
    newResponse = 'placeholder to display a new form to create a new blog'
    return HttpResponse(newResponse)

def create(req):
    return redirect('/main_app')

def show(req, number):
    showResponse = f"Placeholder to display blog {number}."
    return HttpResponse(showResponse)

def edit(req, number):
    showResponse = f"Placeholder to edit blog {number}."
    return HttpResponse(showResponse)

def destroy(req, number):
    return redirect('/main_app')