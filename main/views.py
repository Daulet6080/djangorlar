import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome page")

def user_list(request):
    return HttpResponse("Users list page")


def city_time(request):
    now = datetime.datetime.now()
    return HttpResponse(f"Current server time: {now}")


def counter(request):
    cnt=request.session.get('cnt',0)
    if request.method == 'POST':
        if 'inc' in request.POST:
            cnt += 1
        elif 'reset' in request.POST:
            cnt = 0
        request.session['cnt'] =cnt
    return render(request,'counter.html', {'counter':cnt})


                
    
