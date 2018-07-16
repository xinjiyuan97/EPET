from django.db import models
from django.contrib.auth.models import User
from upload.storage import ImageStorage
from django.utils import timezone
import os
# Create your models here.
def lessonsPath(instance, filename):
    # print(instance.filePath)
    ext = os.path.splitext(filename)[1]
    name = str(instance.resourcesId) +  ext
    return ('%s/%s/%s' % (instance.experimentId, instance.owner, name))

class UploadPhotos(models.Model):
    """
    保存示波器数据
    """
    owner = models.ForeignKey('users.UserInfo', related_name = "experimenter", default = None, on_delete = models.CASCADE)
    filePath = models.ImageField(upload_to = lessonsPath)
    experimentId = models.IntegerField(default = 0)
    resourcesId = models.IntegerField(default = 0)

STATUS = (
    (0, 'On Time'),
    (1, 'Late'),
    (2, 'Waiting')
)

class UploadReport(models.Model):
    owner = models.CharField(max_length = 20)
    filePath = models.FileField('实验报告', upload_to = './report', blank = True)
    lessons = models.CharField(max_length = 200)
    teacher = models.CharField(max_length = 50)
    remark = models.TextField(blank = True) # 作者备注
    comments = models.TextField(blank = True)  # 教师批注
    date = models.DateTimeField(default = timezone.now)
    deadLine = models.DateTimeField(default = timezone.now)

    score = models.IntegerField(default = -1)
    status = models.IntegerField(choices = STATUS, default = 'Waiting')
