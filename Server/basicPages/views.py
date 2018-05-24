from django.shortcuts import render
from .forms import LogInForm, SignUpForm, InformationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from users.models import UserInfo
import hashlib
import Messager.messager as mess
import datetime
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
                return HttpResponseRedirect('/home/')
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
            UserInfo.objects.create(userAccount = user, id = int(username))
            return HttpResponseRedirect('/fillinfo/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def createActiCode(id, tokenExptime):
    # 使用md5生成
    code = id + tokenExptime.strftime("%Y-%m-%d %H:%M:%S")
    md5 = hashlib.md5()
    md5.update(code.encode()) 
    return md5.hexdigest()

def updataInfo(username, name, email, mphone):
    user = UserInfo.objects.get(id = int(username))
    user.name = name
    user.email = email
    user.mphone = mphone
    user.tokenExptime = datetime.datetime.now() + datetime.timedelta(days = 2)
    user.actiCode = createActiCode(username, user.tokenExptime)
    mess.sendVerifyMail(name, email, user.actiCode)
    user.save()

@login_required(login_url='/login/')
def fillInformation(request):
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            updataInfo(form.cleaned_data['username'], form.cleaned_data['name'], \
                form.cleaned_data['email'], form.cleaned_data['mphone'])
            return HttpResponseRedirect('/home/')
    else:
        form = InformationForm({'username': str(request.user)})
    return render(request, 'information.html', {'form': form})