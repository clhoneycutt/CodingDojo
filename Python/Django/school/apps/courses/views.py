from django.shortcuts import render, redirect
from apps.courses.models import *

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    newCourse = request.POST
    Course.objects.create(name=newCourse['course_name'])
    Description.objects.create(content=newCourse['course_desc'])
    return redirect('courses:index')

def remove(request):
    return redirect('courses:index')

def destroy(requset):
    return redirect('courses:index')