from django.shortcuts import render, HttpResponse, redirect
import random, datetime
from time import gmtime, strftime

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    else:
        request.session['gold'] = request.session['gold']

    if 'activities' not in request.session:
        request.session['activities'] = []
    else:
        request.session['activities'] = request.session['activities']
    return render(request, "ninja/index.html")


def requestMoney(request):
    if request.method == "POST":
        location = request.POST['building']
        czas = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        if location == "farm":
            goldF = random.randrange(10, 21)
            info = {'money':goldF, 'place':location, "time": czas}
        elif location == 'cave':
            goldF = random.randrange(5,11)
            info = {'money':goldF, 'place':location, "time": czas}
        elif location == 'house':
            goldF = random.randrange(2,6)
            info = {'money':goldF, 'place':location, "time": czas}
        elif location == 'casino':
            goldF = random.randrange(-50,51)
            info = {'money':goldF, 'place':location, "time": czas}
        
        request.session['activities'].append(info)
        request.session.modified = True
        request.session['gold'] += goldF
    return redirect("/")