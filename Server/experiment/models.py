"""
Title: 实验基本信息
Author: xinjiyuan97
Date: 2018-3-10
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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
    TODO: 用于记录每节课包含哪些实验
    """
    # def getDefaultUser():
    #     return User.objects.get(username = 'admin')

    owner = models.ForeignKey('users.UserInfo', related_name = "ClassOwner", default = None)
    Title = models.CharField(max_length = 200) # 课程名称
    experments = models.TextField() # 包含实验，用Json描述
    
class ExperimentScore(models.Model):
    """
    TODO: 记录完成了哪些实验
    """
    owner = models.ForeignKey('users.UserInfo', related_name = "ScoreOwner", default = None)
    Title = models.CharField(max_length = 200)
    date = models.DateTimeField(default = timezone.now)

REQUESTSTATUS = (
    ('HALT', 'Waiting'),
    ('ON', 'Processing'),
    ('CLOSE', 'Done')
)

STATUS = (
    ('PASS', 'Pass'),
    ('RAW', 'Unjudged'),
    ('REDO', 'Didn\'t pass')
)

class JudgeRequest(models.Model):
    """
    TODO: 审核请求
    """
    owner = models.ForeignKey('users.UserInfo', related_name = "RequestOwner", default = None)
    Title = models.CharField(max_length = 200)
    date = models.DateTimeField(default = timezone.now)
    report = models.TextField()
    requestStatus = models.CharField(
        max_length = 5, 
        choices  = REQUESTSTATUS,
        default = "HALT"
    )
    Status = models.CharField(
        max_length = 4,
        choices  = STATUS,
        default = 'RAW'
    )