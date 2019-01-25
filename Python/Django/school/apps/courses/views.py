from django.shortcuts import render, redirect

def index(request):
    return render(request, 'courses/index.html')

def create(request):
    return redirect('courses:index')

def remove(request):
    return redirect('courses:index')

def destroy(requset):
    return redirect('courses:index')