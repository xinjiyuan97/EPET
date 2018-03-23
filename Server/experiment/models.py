"""
Title: 实验基本信息
Author: xinjiyuan97
Date: 2018-3-10
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Experiments(models.Model):
    """
    TODO: 用于记录每一个大实验中的子实验
    """
    # def getDefaultUser():
    #     return User.objects.get(username = 'admin')

    owner = models.ForeignKey('users.UserInfo', related_name = "ExpermentAuthor", default = None)

    priority = models.IntegerField() # 实验优先级
    Title = models.CharField(max_length = 200) # 实验名称
    description = models.TextField() # 实验描述，用markdown
    expermentScore = models.IntegerField() # 实验满分
    clientView = models.TextField() # 在客户端的视图，用json描述
    reportTemplete = models.TextField() # 实验数据文档模版
    belongs = models.CharField(max_length = 200) # 主实验名称

    def __str__(self):
        return Title

class ContentOfClass(models.Model):
    """
    TODO: 用于记录和查询某个课程记录
    """
    # def getDefaultUser():
    #     return User.objects.get(username = 'admin')

    owner = models.ForeignKey('users.UserInfo', related_name = "Teacher", default = None)

    classNum = models.IntegerField() # 第几节课
    day = models.IntegerField() # 周日 —— 周六 0 - 7
    classRoom = models.CharField(max_length = 50) # 教室
    experment = models.CharField(max_length = 200)

    