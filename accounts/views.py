from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib import messages
from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='userLogin')
def home(request):
    context = {}
    return render(request, 'accounts/home.html', context)

@login_required(login_url='userLogin')
def restaurants(request):
    context = {}    
    return render(request, 'accounts/restaurants.html', context)

@login_required(login_url='userLogin')
def search(request):
    context = {} 
    return render(request, 'accounts/search.html', context)

@login_required(login_url='userLogin')
def profile(request):
    context = {} 
    return render(request, 'accounts/profile.html', context)

def userRegister(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account is created for ' + user + ' succesfully!')
                return redirect('userLogin')

        context = {'form': form} 
        return render(request, 'accounts/userRegister.html', context)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'User or password is incorrect!')

        context = {} 
        return render(request, 'accounts/userLogin.html', context)

@login_required(login_url='userLogin')
def logoutUser(request):
    logout(request)
    return redirect('userLogin')