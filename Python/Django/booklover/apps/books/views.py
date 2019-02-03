from django.shortcuts import render, redirect

def index(req):
    return render(req, 'books/index.html')

def new(req):
    return render(req, 'books/new.html')

def show(req):
    return render(req, 'books/show.html')



def create(req):


    return redirect('books:show')