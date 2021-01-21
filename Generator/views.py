from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'Generator/home.html')

def password(request):

    thepassword = ''
    length = int(request.GET.get('length',10))
    pwd_characters=list('abcdefghijklmnopqrstuvxyz')

    if request.GET.get('uppercase'):
        pwd_characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        pwd_characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        pwd_characters.extend(list('0123456789'))

    for x in range(length):
        thepassword += random.choice(pwd_characters)

    return render(request, 'Generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'Generator/about.html')