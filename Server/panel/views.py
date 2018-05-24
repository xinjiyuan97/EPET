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
    user = {'id': str(request.user), 'name': userInfo.name}
    return render(request, 'panel.html', {'user': user, 'taskList': [], 'notificationList': []})

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')