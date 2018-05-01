"""
Title: 实验信息显示
Author: xinjiyuan97
Date: 2018-3-17
"""

from django.shortcuts import render
from experiment.models import Experiments, ContentOfClass, ExperimentScore, JudgeRequest
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from experiment.serializers import ExperimentSerializer, ExperimentTitleSerializer, LessonsSerializer, ScoreSerializer, JudgeRequestSerializer
from rest_framework.views import APIView
from utils.permissions import IsOwnerOrReadOnly, IsTeacher
from users.models import UserInfo

# Create your views here.
def getAllExperiments():
    experiments = Experiments.objects.all()
    return experiments

def getExperiment(title):
    try:
        experiment = Experiments.objects.filter(belongs = title)
    except Users.DoesNotExist as e:
        return None
    return experiment

class ShowAllExperiments(generics.ListAPIView):
    queryset = getAllExperiments()
    serializer_class = ExperimentTitleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    

class ShowExperiment(generics.RetrieveAPIView):
    # def get(self, request, format = None):
    #     title = request.data['title']
    #     experiment = getExperiment(title)
    #     serializer = ExperimentSerializer(experiment.data, many = True)
    #     return Response(serializer.data)

    queryset = Experiments.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    lookup_field = 'id'
    def perform_create(self, serializer):
        serializer.save(userAccount = self.request.user)

class ModifiyExperiment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiments.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    lookup_field = 'id'
    def perform_create(self, serializer):
        serializer.save(userAccount = self.request.user)

class AddExperiment(generics.CreateAPIView):
    queryset = getAllExperiments()
    serializer_class = ExperimentSerializer
    
    permission_classes = (permissions.IsAuthenticated, IsTeacher)
    def perform_create(self, serializer):
        serializer.save(owner = UserInfo.objects.get(userAccount = self.request.user))
    # 

class AddALesson(generics.CreateAPIView):
    queryset = ContentOfClass.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (IsTeacher,)

    def perform_create(self, serializer):
        userInfo = UserInfo.objects.get(userAccount = self.request.user)
        
        if userInfo.userType != 'TR':
            return Response(status = status.HTTP_403_FORBIDDEN)
        # 这块儿权限实在不知道怎么处理了
        serializer.save(owner = UserInfo.objects.get(userAccount = self.request.user))

class UpdateLessons(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentOfClass.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    # permission_classes = (IsTeacher,)
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(owner = UserInfo.objects.get(userAccount = self.request.user))

class ListAllLessons(generics.ListAPIView):
    queryset = ContentOfClass.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

class Submit(generics.CreateAPIView):
    queryset = JudgeRequest.objects.all()
    serializer_class = JudgeRequestSerializer
    permission_classes = (IsTeacher, )

    def perform_create(self, serializer):
        serializer.save(owner = UserInfo.objects.get(userAccount = self.request.user))

