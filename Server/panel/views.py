from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UserInfo
from experiment.models import ContentOfClass, Experiments
from django.contrib import auth
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User
import json
from .forms import InformationForm, ChangePwdForm
from upload.forms import UploadReportForm
from upload.models import UploadReport
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

def getAllexperiments(expList):
    '''TODO: 获取一个课程中的所有试验'''
    res = []
    for item in expList:
        exp = Experiments.objects.get(id = item)
        res.append(exp)
    return res

@login_required(login_url='/login/')
def experiment(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    id = request.GET.get('id', None)
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    if id:
        id = int(id)
        exp = {}
        lesson = []
        experiments = ContentOfClass.objects.get(id = id)
        exp['title'] = experiments.title
        expList = json.loads(experiments.experments)
        exp['experiments'] = getAllexperiments(expList)
        return render(request, 'expContent.html', {'user': user, 'taskList': [], 'notificationList': [], 'exp': exp})
    else:
        experiments = ContentOfClass.objects.all()
        return render(request, 'experiment.html', {'user': user, 'taskList': [], 'notificationList': [], 'experimentList': experiments})

def getObject(L): # 用于筛选未交的实验报告
    res = []
    for item in L:
        if item.status == 2:
            res += [(item.id, item.lessons)]
    return res

@login_required(login_url='/login/')
def report(request):
    """ 实验报告　"""
    if request.method == 'POST':
        form = UploadReportForm(request.POST, request.FILES)
        if form.is_valid():
            lessons = form.cleaned_data['lessons']
            
            # rep = UploadReport.objects.get(owner = int(str(request.user)), )
    else:
        form = UploadReportForm()
        
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    report = UploadReport.objects.filter(owner = int(str(request.user)))
    form.fields['lessons'].choices = getObject(report)
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'report.html', {'user': user, 'taskList': [], 'notificationList': [], 'report': report, 'form': form})

@login_required(login_url='/login/')
def score(request):
    """ 显示实验成绩　"""
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'score.html', {'user': user, 'taskList': [], 'notificationList': [], 'report': report})

@login_required(login_url='/login/')
def data(request):
    """ 显示实验数据　"""
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'data.html', {'user': user, 'taskList': [], 'notificationList': [], 'report': report})

@login_required(login_url='/login/')
def userInfo(request):
    """ 显示用户个人信息　"""
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    return render(request, 'userInfo.html', {'user': userInfo, 'taskList': [], 'notificationList': [], 'report': report})


""" 
分别为设置用户个人信息、重置密码
"""

@login_required(login_url='/login/')
def settings(request):

    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            userInfo.mPhone = form.cleaned_data['mPhone']
            userInfo.email = form.cleaned_data['email']
            userInfo.school = form.cleaned_data['school']
            userInfo.major = form.cleaned_data['major']
            userInfo.save()
            return HttpResponseRedirect('/settings/')
    else:
        # print(userInfo.__dict__)
        form = InformationForm(userInfo.__dict__)
    formPwd = ChangePwdForm({'username': str(request.user)})
    return render(request, 'settings.html', {'user': userInfo, 'taskList': [], 'notificationList': [], 'report': report, 'form0': form, 'form1': formPwd})

@login_required(login_url = '/login/')
def settingPass(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    if request.method == 'POST':
        formPwd = ChangePwdForm(request.POST)
        if formPwd.is_valid():
            username = formPwd.cleaned_data['username']
            password = formPwd.cleaned_data['password']
            user = User.objects.get(username = username)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/settings/')
    else:
        return HttpResponseRedirect('/settings/')
    form = InformationForm(userInfo.__dict__)
    return render(request, 'settings.html', {'user': userInfo, 'taskList': [], 'notificationList': [], 'report': report, 'form0': form, 'form1': formPwd})

@login_required(login_url='/login/')
def aboutUs(request):
    userInfo = UserInfo.objects.get(id = int(str(request.user)))
    user = {'id': str(request.user), 'name': userInfo.name, 'usertype': userInfo.userType}
    return render(request, 'aboutUs.html', {'user': user, 'taskList': [], 'notificationList': [], 'report': report})