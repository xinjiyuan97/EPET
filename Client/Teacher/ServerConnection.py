import requests

API = 'http://139.199.24.250/api/'

global user,pswd
user=''
pswd=''

#用户登录
def login(username,passwd):
    global user,pswd
    url=API+'login/'
    d = {'username': username, 'password': passwd}
    req = requests.post(url, data=d)
    status=req.status_code
    #print(status)
    if status==202:
        user=int(username)
        pswd=passwd
        return True
    else:
        return False

#用户注册
def register(username,passwd):
    url=API+'register/'
    d = {'username': username, 'password': passwd}
    req=requests.post(url,data=d)
    status=req.status_code
    if status==202:
        return True
    else:
        return False

#用户登出
def logout():
    url=API+'logout/'
    req=requests.post(url)
    status=req.status_code
    if status==202:
        return True
    else:
        return False


#获取用户信息
def Get_UserInfo():
    url=API+'userinfo/'
    req=requests.get(url)
    status=req.status_code
    if status==200:
        UserList=req.json()
        for i in range(len(UserList)):
            if UserList[i]['id']==user:
                UserInfo=UserList[i]
                break
        return UserInfo
    else:
        return False

#更新用户信息
def Update_UserInfo(UserInfo):
    url=API+'register/completeInfo/' + str(user)
    req=requests.put(url,data=UserInfo)
    status=req.status_code
    if status==200:
        return True
    else:
        return False

#开放实验室
def LabRegister(ClassRoom):
    url=API+'lab/register/'
    d={"labNum":ClassRoom,"labStatus":'OPEN'}
    req=requests.post(url,data=d,auth=(user,pswd))
    Status=req.status_code
    print(Status)
    if Status==201:
        return True
    else:
        return False
    
#实验室列表
def LabList():
    url=API+'lab/list/'
    req=requests.get(url,auth=(user,pswd))
    Status=req.status_code
    if Status==200:
        return req.json()
    else:
        return None

#实验室状态更新
def LabUpdate(Lab,Status):
    url=API+'lab/update/%d/' % Lab['id']
    Lab['labStatus']='CLOSE'
    req=requests.put(url,data=Lab,auth=(user,pswd))
    Status=req.status_code
    if Status==200:
        return True
    else:
        return False

def UpdateRequest(StuReq,Status):
    url=API+'student/update/%d/' % StuReq['id']
    StuReq.pop('id')
    StuReq['requestStatus']='CLOSE'
    req=requests.put(url,data=StuReq,auth=(user,pswd))
    Status=req.status_code
    if Status==200:
        return True
    else:
        return False
    
def StudentRequest(LabNum):
    url=API+'student/list/?labNum=%d' % LabNum
    print(url)
    req=requests.get(url,auth=(user,pswd))
    Status=req.status_code
    if Status==200:
        return req.json()
    else:
        return False

def UpdateRequest(StuReq,Status):
    url=API+'student/update/%d/' % StuReq['id']
    StuReq.pop('id')
    StuReq['requestStatus']='CLOSE'
    req=requests.put(url,data=StuReq,auth=(user,pswd))
    
        
login('88881154','980323')
