from django.shortcuts import render, redirect
from django.contrib import messages
from apps.courses.models import *

def index(request):
    courses = Course.objects.all()
    for course in courses:
        course = course.__dict__
        desc = Description.objects.get(id=course['description_id'])
        desc = desc.__dict__
        desc = desc['content']
        course['desc'] = desc
        course['id'] = course['description_id']    
    context = {
        'courses': courses,
    }
    return render(request, 'courses/index.html', context)

def create(request):
    newCourse = request.POST
    errors = Course.objects.validate(newCourse)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('courses:index')
    else:
        desc = Description.objects.create(content=newCourse['desc'])
        Course.objects.create(name=f"{newCourse['name']}", description=desc)
        return redirect('courses:index')

def remove(request, course_id):
    course = Course.objects.get(description_id=course_id)
    course = course.__dict__
    desc = Description.objects.get(id=course['description_id'])
    desc = desc.__dict__
    desc = desc['content']
    course['desc'] = desc
    course['id'] = course['description_id']
    context = {
        'course': course
    }
    
    return render(request, 'courses/confirm.html', context)

def destroy(request, course_id):
    goner = Course.objects.get(description_id=course_id)
    goner.delete()
    return redirect('courses:index')