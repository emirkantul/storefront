from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from difflib import SequenceMatcher
import sys
import logging
import string 
import numpy as np
def logout(request):
    auth.logout(request)
    return redirect('index')
def containsNumber(value):
    if True in [char.isdigit() for char in value]:
        return True
    return False
def Upper(value):
    if True in [char.isupper() for char in value]:
        return True
    return False
def punc(value):
    for i in value:
        if i in string.punctuation:
            return True
    return False      

def index(request):
    return render(request,'index.html')


def rez(request):
    return render(request,'rez.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if '@' not in username or '.' not in username:
            messages.info(request, 'This looks like an incorrect address')
            return redirect('signin') 
        elif(user is not None):
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Credentials are invalid!")
            return redirect('signin')
    else:
        return render(request,"signin.html")


def register(request):
     if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        if '@' not in username or '.' not in username:
            messages.info(request, 'This looks like an incorrect address')
            return redirect('register') 
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Email already used')
            return redirect('register')
        elif len(password) < 8 or not containsNumber(password) or not Upper(password) or not punc(password):
            messages.info(request, ' Password should be at least 6 characters')
            messages.info(request,' Upper/lower case letters')
            messages.info(request,' Number or punctuation')
            return redirect('register')      
        else:
            user = User.objects.create_user(username=username,password=password)
            user.save()
            user = auth.authenticate(username=username,password=password)
            auth.login(request,user)
            return render(request,'index.html')
     else:
        return render(request,'register.html')

