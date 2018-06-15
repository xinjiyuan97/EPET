from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UserInfo
from django.contrib import auth
from django.http import HttpResponseRedirect 
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    if not userInfo.name:
        return HttpResponseRedirect('/fillinfo/')
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'home.html', {'user': user, 'taskList': [], 'notificationList': []})

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def syllabus(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'syllabus.html', {'user': user, 'taskList': [], 'notificationList': []})

@login_required(login_url='/login/')
def experiment(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'experiment.html', {'user': user, 'taskList': [], 'notificationList': [], 'experimentList': experiment})

@login_required(login_url='/login/')
def report(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'report.html', {'user': user, 'taskList': [], 'notificationList': [], 'report': report})

@login_required(login_url='/login/')
def score(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'score.html', {'user': user, 'taskList': [], 'notificationList': [], 'report': report})

@login_required(login_url='/login/')
def data(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'data.html', {'user': user, 'taskList': [], 'notificationList': [], 'report': report})

@login_required(login_url='/login/')
def aboutUs(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'aboutUs.html', {'user': user, 'taskList': [], 'notificationList': [], 'report': report})