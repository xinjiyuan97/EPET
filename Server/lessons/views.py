from django.shortcuts import render
from lessons.models import LabServers, StudentRequests
from rest_framework import generics
from rest_framework import permissions
from lessons.serializers import LabServerSerializer, StudentRequestSerializer
from rest_framework.views import APIView
from utils.permissions import IsOwnerOrReadOnly, IsTeacher, IsOwner
from users.models import UserInfo
from django.core.exceptions import ValidationError
# Create your views here.

class ServerRegister(generics.CreateAPIView):
    queryset = LabServers.objects.all()
    serializer_class = LabServerSerializer
    
    permission_classes = (IsTeacher, )
    def perform_create(self, serializer):
        userInfo = UserInfo.objects.get(userAccount = self.request.user)
        if userInfo.userType != 'TR':
            raise ValidationError('The action is forbidden!')
        # 这块儿权限实在不知道怎么处理了
        serializer.save(owner = UserInfo.objects.get(userAccount = self.request.user))

class ServerUpdate(generics.UpdateAPIView):
    queryset = LabServers.objects.all()
    serializer_class = LabServerSerializer
    
    permission_classes = (IsOwner, )
    lookup_field = 'id'
    def perform_create(self, serializer):
        serializer.save(owner = UserInfo.objects.get(userAccount = self.request.user))

class ServerList(generics.ListAPIView):
    queryset = LabServers.objects.filter(labStatus = 'OPEN')
    serializer_class = LabServerSerializer
    
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    
class SendStudentRequest(generics.CreateAPIView):
    queryset = StudentRequests.objects.all()
    serializer_class = StudentRequestSerializer

    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner = UserInfo.objects.get(userAccount = self.request.user))

class FillStudentRequest(generics.UpdateAPIView):
    queryset = StudentRequests.objects.all()
    serializer_class = StudentRequestSerializer
    lookup_field = 'id'
    permission_classes = (IsTeacher, )

class ListUndoStudentRequest(generics.ListAPIView):
    def get_queryset(self):
        userInfo = UserInfo.objects.get(userAccount = self.request.user)
        if userInfo.userType != 'TR':
            raise ValidationError('The action is forbidden!')

        lab = self.request.GET['labNum']
        queryset = StudentRequests.objects.filter(labNum = lab, requestStatus = 'HALT')
        queryset
        return queryset
    serializer_class = StudentRequestSerializer

    permission_classes = (IsTeacher, )

class GetRespond(generics.RetrieveAPIView):
    queryset = StudentRequests.objects.filter(requestStatus = 'CLOSE')
    serializer_class = StudentRequestSerializer
    lookup_field = 'id'
    permission_classes = (IsOwner, )