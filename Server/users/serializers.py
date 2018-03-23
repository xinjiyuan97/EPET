"""
Title: 用户信息序列化
Author: xinjiyuan97
Date: 2018-3-10
"""
from rest_framework import serializers
from users.models import UserInfo, USERTYPE
from django.contrib.auth.hashers import make_password
from experiment.models import ContentOfClass
import datetime
import Messager.messager as mess
from django.contrib.auth.models import User
import hashlib

class UserInfoSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source = 'userAccount.username')
    # 用于制作token
    def createActiCode(self, instance):
        # 使用md5生成
        code = str(instance.id) + instance.tokenExptime.strftime("%Y-%m-%d %H:%M:%S")
        md5 = hashlib.md5()
        md5.update(code.encode()) 
        return md5.hexdigest()

    def create(self, validatedData):
        return UserInfo.objects.create(**validatedData)

    def update(self, instance, validatedData):
        if instance.status == False or instance.email != validatedData['email']:
            instance.tokenExptime = datetime.datetime.now() + datetime.timedelta(days = 7)
            instance.actiCode = self.createActiCode(instance)
            instance.status = False
            mess.sendVerifyMail(validatedData['name'], validatedData['email'], instance.actiCode)
        instance.name = validatedData.get('name', instance.name)
        instance.email = validatedData.get('email', instance.email)
        instance.mPhone = validatedData.get('mPhone', instance.mPhone)
        instance.save()
        return instance

    class Meta:
        model = UserInfo
        fields = ('id', 'username', 'name', 'email', \
            'mPhone', 'userType', 'status', 'actiCode', \
            'tokenExptime')

class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validatedData):
        validatedData['password'] = make_password(validatedData['password'])
        user = User(**validatedData)
        user.save()
        UserInfo.objects.create(userAccount = user, id = validatedData['username'])
        
        return user

    class Meta:
        model = User
        fields = ('username', 'password')

class UserSerializer(serializers.ModelSerializer):
    # userInfo = serializers.PrimaryKeyRelatedField(many=True, queryset = UserInfo.objects.all())
    def create(self, validatedData):
        validatedData['password'] = make_password(validatedData['password'])
        return User.objects.create(**validatedData)

    class Meta:
        model = User
        fields = ('username', 'password')

"""
{
  "ID": 11111, 
  "name": "张三",
  "password": "12345678",
  "email": "zhangsan@1234.567",
  "mPhone": "12345678910",
  "userType": "SD"
}
"""