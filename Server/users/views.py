"""
Title: 用户个人信息处理
Author: xinjiyuan97
Date: 2018-3-18
"""
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserInfoSerializer, UserSerializer, UserCreateSerializer
from rest_framework import status
from django.http import Http404, HttpResponse
from users.models import UserInfo
import users.emailConfirm as emcf
from utils.UserError import WrongPassword
from utils.permissions import IsOwner
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def varify(request):
    # TODO: 用户邮箱Token验证
    token = request.GET['actiCode']
    # print(token)
    html = emcf.confirm(request, token)
    return html

def checkPassword(user, password):
    print('ckpt')
    print(user.ID, user.password)
    print(password)
    if user.password != password:
        raise WrongPassword()

# def setSession(user, request):
#     request.session['userID'] = user.ID
#     return request

class UsersList(generics.ListCreateAPIView):
    # TODO 显示所有用户（Debug时使用）
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserInfoList(generics.ListCreateAPIView):
    # TODO 显示所有用户（Debug时使用）
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class CompleteUserInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    
    lookup_field = 'id'
    def perform_create(self, serializer):
        serializer.save(userAccount = self.request.user)

class UserRegister(generics.CreateAPIView):
    # TODO 用户注册

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    # def post(self, request, format = None):
    #     serializer = UserRegisterSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
            
    #         return Response(serializer.data, status = status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request, format = None):
        username = request.data['username']
        password = request.data['password']
        user = auth.authenticate(username = username, password = password) 
        print(user)
        if user:
            auth.login(request, user)
            return Response(status = status.HTTP_202_ACCEPTED)
        else:
            return Response(status = status.HTTP_406_NOT_ACCEPTABLE)

class UserModifyPassword(APIView):
    def post(self, request, format = None):
        pass


    