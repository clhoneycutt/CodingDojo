from django.shortcuts import render, redirect
from .models import Message, Comment

def index(request):
    if not request.session['loggedIn']:
        return redirect('main:index')

    return render(request, 'theWall/index.html')

def postMessage(request):
    if not request.session['loggedIn']:
        return redirect('main:index')
    
    if request.method == 'POST':
        messageInfo = request.POST
        errors = Message.objects.validateMsg(messageInfo)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('thewall:index')

        userid = request.session['userid']
        Message.objects.addMessage(messageInfo, userid)
        return redirect('thewall:index')
    else:
        return redirect('thewall:index')