"""
Title: 用户个人信息数据库
Author: xinjiyuan97
Date: 2018-3-10
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

USERTYPE = (
    ('TR', 'Teacher'),
    ('SD', 'Student'),
) 
    
# Create your models here.
class UserInfo(models.Model):
    # pk = models.Field()
    # 用户个人信息
    id = models.IntegerField(primary_key = True)
    userAccount = models.OneToOneField(User, on_delete = models.CASCADE) # 学号
    name = models.CharField(max_length = 50) # 姓名
    # password = models.CharField(max_length = 50) # 密码
    email = models.EmailField() # 邮箱
    mPhone = models.CharField(max_length = 20) # 手机号
    userType = models.CharField(
        max_length = 2, 
        choices = USERTYPE, 
        default = 'SD'
    )

    # 邮箱验证部分
    status = models.BooleanField(default = False) # 是否通过邮箱验证
    actiCode = models.CharField(max_length = 200, default = "NULL") # 激活码
    tokenExptime = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return str(self.id)