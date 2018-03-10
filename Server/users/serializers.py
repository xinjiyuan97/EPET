"""
Title: 用户信息序列化
Author: xinjiyuan97
Date: 2018-3-10
"""
from rest_framework import serializers
from users.models import Users, USERTYPE

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('ID', 'name', 'password', 'email', 'mPhone', 'userType')