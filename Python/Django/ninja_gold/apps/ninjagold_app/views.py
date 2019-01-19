from django.shortcuts import render, redirect
from random import randrange
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninjagold_app/index.html')

def farm(request):
    # Create Timestamp
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y %I:%M %p")
    
    # calculate win/loss
    farm_gain = randrange(10, 20)
    request.session['gold'] += farm_gain
    
    # generate activity log
    request.session['activities'].insert(0, {'win_loss': farm_gain, 'location': 'farm', 'color': 'green', 'timestamp': timestamp})
    return redirect('/')

def cave(request):
    # Create Timestamp
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y %I:%M %p")

    # calculate win/loss
    cave_gain = randrange(5, 10)
    request.session['gold'] += cave_gain

    # generate activity log
    request.session['activities'].insert(0, {'win_loss': cave_gain, 'location': 'cave', 'color': 'green', 'timestamp': timestamp})
    return redirect('/')

def house(request):
    # Create Timestamp
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y %I:%M %p")

    # calculate win/loss
    house_gain = randrange(2, 5)
    request.session['gold'] += house_gain

    # generate activity log
    request.session['activities'].insert(0, {'win_loss': house_gain, 'location': 'house', 'color': 'green', 'timestamp': timestamp})
    return redirect('/')

def casino(request):
    # Create Timestamp
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y %I:%M %p")

    # calculate win/loss
    gamble = randrange(-50, 50)
    request.session['gold'] += gamble

    # generate activity log
    if gamble >= 0:
        color = 'green'
    else:
        color = 'red'
    request.session['activities'].insert(0, {'win_loss': gamble, 'location': 'casino', 'color': color, 'timestamp': timestamp})
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')