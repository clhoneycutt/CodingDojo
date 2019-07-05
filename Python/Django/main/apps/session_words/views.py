from django.shortcuts import render, redirect
from datetime import datetime

def index(req):
    if 'word' in req.session:
        print(req.session['words'])

    return render(req, 'session_words/index.html')


def add_word(req):
    if req.method == 'POST':
        if 'big' in req.POST:
            showbig = "font-size: 1.5em;"
        else:
            showbig = ""

        if 'words' not in req.session:
            req.session['words'] = []

        now = datetime.now()
        timestamp = now.strftime("%m/%d/%Y %I:%M %p")


        temp_list = req.session['words']
        
        temp_list.append({"word": req.POST['new_word'], "color": req.POST['color'], "show_big": showbig, "added": timestamp},)
        
        req.session['words'] = temp_list
        print(req.session['words'])
    req.session.modified = True
    return redirect('/session_words')

def clear_session(req):
    req.session.clear()
    return redirect('/session_words')
