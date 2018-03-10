"""
Title: 用户个人信息数据库
Author: xinjiyuan97
Date: 2018-3-10
"""

from django.db import models

USERTYPE = (
    ('TR', 'Teacher'),
    ('SD', 'Student'),
) 
    
# Create your models here.
class Users(models.Model):
    ID = models.IntegerField(primary_key = True) # 学号
    name = models.CharField(max_length = 50) # 姓名
    password = models.CharField(max_length = 50) # 密码
    email = models.EmailField() # 邮箱
    mPhone = models.CharField(max_length = 20) # 手机号
    userType = models.CharField(
        max_length = 2, 
        choices = USERTYPE, 
        default = 'SD'
    )
    class Meta:
        ordering = ('ID', )