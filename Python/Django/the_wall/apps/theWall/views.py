from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message, Comment

def index(request):
    if not request.session['loggedIn'] or 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
        return redirect('main:index')
    context = {
    'allMessages': Message.objects.all().order_by("-created_at")
    }
    return render(request, 'theWall/index.html', context)

def post_message(request):
    if not request.session['loggedIn']:
        request.session['loggedIn'] = False
        return redirect('main:index')
    
    if request.method == 'POST':
        messageInfo = request.POST
        errors = Message.objects.validateMsg(messageInfo)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('thewall:index')

        userid = request.session['userid']
        Message.objects.addMessage(messageInfo)
        return redirect('thewall:index')
    else:
        return redirect('thewall:index')

def post_comment(request):
    if not request.session['loggedIn']:
        request.session['loggedIn'] = False
        return redirect('main:index')

    if request.method == 'POST':
        commentInfo = request.POST
        errors = Comment.objects.validateComment(commentInfo)
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('thewall:index')

        userid = request.session['userid']
        Comment.objects.addComment(commentInfo)
        return redirect('thewall:index')
    else:
        return redirect('thewall:index')