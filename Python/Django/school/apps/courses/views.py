from django.shortcuts import render, redirect
from apps.courses.models import *

def index(request):
    courses = Course.objects.all()
    for course in courses:
        course = course.__dict__
        desc = Description.objects.get(id=course['description_id'])
        desc = desc.__dict__
        desc = desc['content']
        course['desc'] = desc
        print(course)
    context = {
        'courses': courses,
    }
    return render(request, 'courses/index.html', context)

def create(request):
    newCourse = request.POST
    print(newCourse)
    desc = Description.objects.create(content=newCourse['desc'])
    Course.objects.create(name=f"{newCourse['name']}", description=desc)
    return redirect('courses:index')

def remove(request, course_id):
    courses = Course.objects.get(id=course_id)
    print(courses)
    return render(request, 'courses/confirm.html')

def destroy(request):
    return redirect('courses:index')