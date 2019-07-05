from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
    return render(request, 'main/index.html')


def generate_num(request):
    if request.method == 'POST':
        if request.session['attempt'] == 0:
            request.session['attempt'] = 1
        else:
            request.session['attempt'] += 1
        request.session['random_str'] = get_random_string(length=14)
        return redirect('/')
    else:
        return redirect('/')