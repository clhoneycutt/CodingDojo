from django.shortcuts import render, redirect
from apps.courses.models import *

def index(request):
    context = {
        'courses': Course.objects.all()
    }

    return render(request, 'courses/index.html', context)

def create(request):
    newCourse = request.POST
    print(newCourse)
    desc = Description.objects.create(content=newCourse['course_desc'])
    Course.objects.create(name=f"{newCourse['course_name']}", description=desc)
    return redirect('courses:index')

def remove(request, course_id):
    return redirect('courses:index')

def destroy(requset):
    return redirect('courses:index')