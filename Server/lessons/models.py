from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

SERVERSTATUS = (
    ('OPEN', 'Running'),
    ('CLOSE', 'Stop')
)

REQUESTSTATUS = ( # 请求处理进度
    ('HALT', 'Waiting'),
    ('ON', 'Processing'),
    ('CLOST', 'Done')
)

REQUESTCLASSES = ( # 请求类型
    ('CI', 'ChechIn'),
    ('CO', 'CheckOut'),
    ('RQ', 'Request')
)

RESPONSECLASSES = ( # 返回类型
    ('JPEG', 'Jpeg Image'),
    ('CSV', 'CSV File'),
    ('TEXT', 'Text Response'),
    ('HTTP', 'A http file')
)

class LabServers(models.Model):
    """
    TODO: 用于记录实验室教师机在线情况
    """
    owner = models.ForeignKey('users.UserInfo', related_name = "Teacher", default = None)
    labNum = models.CharField(max_length = 200) # 实验室门牌号
    date = models.DateTimeField(default = timezone.now)
    labStatus = models.CharField(
        max_length = 5,
        choices = SERVERSTATUS, 
        default = 'OPEN'
    )


    def __str__(self):
        return labNum

class StudentRequests(models.Model):
    """
    TODO: 处理学生端请求事务
    """
    owner = models.ForeignKey('users.UserInfo', related_name = "Student", default = None)
    labNum = models.CharField(max_length = 200) # 实验室门牌号
    tableNum = models.IntegerField() # 学生桌号
    date = models.DateTimeField(default = timezone.now) # 请求发送时间
    requestClasses = models.CharField( # 请求类型
        max_length = 2,
        choices = REQUESTCLASSES,
        default = 'RQ',
    )
    reponseContent = models.TextField(null = True) # 响应内容
    reponseClasses = models.CharField( # 响应类型
        max_length = 4, 
        choices = RESPONSECLASSES,
        default = 'TEXT',
    )
    requestStatus = models.CharField( # 响应状态
        max_length = 5,
        choices = REQUESTSTATUS,
        default = 'HALT',
    )