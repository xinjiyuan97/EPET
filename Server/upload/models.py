from django.db import models
from django.contrib.auth.models import User
from upload.storage import ImageStorage
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