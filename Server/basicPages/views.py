from django.shortcuts import render
from .forms import LogInForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')

def pageNotFound(request):
    return render(request, 'errorPage.html', {'errorCode': 404})

def permissionDenied(request):
    return render(request, 'errorPage.html', {'errorCode': 403})

def pageError(request):
    return render(request, 'errorPage.html', {'errorCode': 500})

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username = username, password = password)
            if user is not None or user.is_active():
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username = username, password = password)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})