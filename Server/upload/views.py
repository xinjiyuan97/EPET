from django.shortcuts import render
from upload.serializers import OscilloscopeSerializer
from upload.models import UploadPhotos
from utils.permissions import IsOwnerOrReadOnly, IsTeacher
from rest_framework import permissions
from rest_framework import generics
from users.models import UserInfo
# Create your views here.
class uploadOscilloscope(generics.CreateAPIView):
    queryset = UploadPhotos.objects.all()
    serializer_class = OscilloscopeSerializer
    
    permission_classes = (permissions.IsAuthenticated, IsTeacher)
    
    def perform_create(self, serializer):
        # print(serializer)
        serializer.save(owner = UserInfo.objects.get(userAccount = self.request.user))
