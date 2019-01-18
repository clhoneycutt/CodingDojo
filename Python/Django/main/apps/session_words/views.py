from django.shortcuts import render, redirect

def index(req):
    if 'word' in req.session:
        print(req.session['words'])

    return render(req, 'session_words/index.html')


def add_word(req):
    if req.method == 'POST':
        if 'big' in req.POST:
            showbig = 1
        else:
            showbig = 0

        if 'words' not in req.session:
            req.session['words'] = []

        temp_list = req.session['words']
        
        temp_list.append({"word": req.POST['new_word'], "color": req.POST['color'], "show_big": showbig})
        
        req.session['words'] = temp_list
        print(req.session['words'])
    req.session.modified = True
    return redirect('/session_words')

def clear_session(req):
    req.session.clear()
    return redirect('/session_words')
