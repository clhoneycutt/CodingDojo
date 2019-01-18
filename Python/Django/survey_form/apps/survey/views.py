from django.shortcuts import render, redirect

# Create your views here.

def index(req):
    return render(req, 'survey/index.html')

def process(req):
    if req.method == 'POST':
        if 'counter' not in req.session:
            req.session['counter'] = 1
        else:
            req.session['counter'] += 1
        req.session['form_data'] = req.POST
        return redirect('/result')
    else:
        return redirect('/')    


def result(req):
    context = {
        'name': req.session['form_data']['name'],
        'location': req.session['form_data']['location'],
        'fav_lang': req.session['form_data']['fav_lang'],
        'comment': req.session['form_data']['comment'],
        'counter': req.session['counter']
    }
    print(context)
    return render(req, 'survey/result.html', context)