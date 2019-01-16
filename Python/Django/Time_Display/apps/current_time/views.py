from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y %I:%M %p")
    context = {
        'timestamp' : timestamp
    }
    return render(request, 'current_time/index.html', context)

